import asyncio
import json
from deep_translator import GoogleTranslator
from textual.app import App, ComposeResult
from textual.widgets import Header, Label, Input, Button, Checkbox, Footer, ListView, ListItem
from textual.containers import Container
from textual.validation import Number

class Kevin_Santos_IO(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "Textual.tcss"

    def __init__(self):
        super().__init__()
        self.step = "name"
        self.user_name = ""
        self.user_age = ""
        self.languages = []
        self.theme = "nord"

    def age_capabilities(self, age: int) -> str:
        caps = {
            "Drive (typical US)": age >= 16,
            "Vote (US)": age >= 18,
            "Drink (US)": age >= 21,
            "Rent a car easily (US)": age >= 25,
            "Run for President (US)": age >= 35,
        }
        check = []
        for label, ok in caps.items():
            check.append(f"{'ELIGIBLE' if ok else 'VOID----'} {label}")
        return "\n".join(check)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with Container(id="main_container"):
            with Container(id="welcomeBox"):
                yield Input(placeholder="Please enter your name", id="nameInput", type="text")
                yield Button("Send", id="submit_button")
            with Container(id="outputBox"):
                yield Label("Welcome! Responses will appear here", id="outputLabel")
                yield ListView(id="ageList", classes="hidden")
            with Container(id="checkboxBox", classes="hidden"):
                yield Label("Select the languages to translate your phrase:", id="checkboxLabel")

    async def translate(self, text: str, target_language: str) -> str:
        def sync_translate():
            translator = GoogleTranslator(source='auto', target=target_language)
            return translator.translate(text)
        loop = asyncio.get_running_loop()
        translation_dream = loop.run_in_executor(None, sync_translate)
        translation = await translation_dream
        print(f"Translation to {target_language}: {translation}")
        return translation

    async def on_button_pressed(self, event: Button.Pressed):
        print(f"Button pressed: {event.button.id}, Current step: {self.step}")
        output_label = self.query_one("#outputLabel")
        welcome_box = self.query_one("#welcomeBox")
        checkbox_box = self.query_one("#checkboxBox")
        age_list = self.query_one("#ageList", ListView)

        if event.button.id == "submit_button" and self.step == "name":
            self.user_name = self.query_one("#nameInput").value.strip()
            if not self.user_name:
                output_label.update("Please enter a valid name.")
                return
            output_label.update(f"Hello, {self.user_name}! Please enter your age!")
            name_input = self.query_one("#nameInput")
            name_input.clear()
            name_input.validators = [Number()]
            name_input.placeholder = "Please enter your age (integers only!)"
            self.step = "age"

        elif event.button.id == "submit_button" and self.step == "age":
            name_input = self.query_one("#nameInput")
            self.user_age = name_input.value.strip()
            if not self.user_age.isdigit():
                output_label.update("Please enter a valid age (integers only).")
                return
            self.user_age = int(self.user_age)

            age_info = [
                f"Age: {self.user_age}",
                "Capabilities:"
            ] + [cap for cap in self.age_capabilities(self.user_age).split("\n")]
            age_list.clear()
            for item in age_info:
                age_list.append(ListItem(Label(item)))
            age_list.remove_class("hidden")
            output_label.update("Now list up to 5 languages wish to learn")  # Added separator
            name_input.clear()
            name_input.placeholder = "e.g. Spanish,Japanese"
            name_input.validators = []
            self.step = "language"

        elif event.button.id == "submit_button" and self.step == "language":
            age_list.add_class("hidden")
            name_input = self.query_one("#nameInput")
            langs = [s.strip().lower() for s in name_input.value.split(",") if s.strip()]
            if not langs:
                output_label.update("Please enter at least one language (comma-separated).")
                return
            if len(langs) > 5:
                output_label.update("Please enter up to 5 languages only.")
                return
            lang_map = {
                "english": "en", "spanish": "es", "french": "fr", "chinese": "zh-CN",
                "german": "de", "japanese": "ja", "russian": "ru", "italian": "it",
                "vietnamese": "vi", "portuguese": "pt"
            }
            self.languages = []
            invalid_langs = []
            for lang in langs:
                if lang in lang_map:
                    self.languages.append((lang, lang_map[lang]))
                else:
                    invalid_langs.append(lang)
            if not self.languages:
                output_label.update(f"No valid languages provided. Unrecognized: {', '.join(invalid_langs)}")
                return
            output_label.update(f"You listed {len(self.languages)} language(s): {', '.join([lang[0] for lang in self.languages])}")
            name_input.clear()
            name_input.placeholder = "e.g. I love Advanced CS"
            output_label.update("Enter a phrase you wish to learn")
            self.step = "phrase"

        elif event.button.id == "submit_button" and self.step == "phrase":
            self.targetTranslation = self.query_one("#nameInput").value.strip()
            if not self.targetTranslation:
                output_label.update("Please enter a phrase to learn.")
                return
            output_label.update(f"Phrase to translate: {self.targetTranslation}")
            welcome_box.add_class("hidden")
            checkbox_box.remove_class("hidden")
            for widget in checkbox_box.query(Checkbox):
                widget.remove()
            for lang_name, _ in self.languages:
                checkbox_box.mount(Checkbox(lang_name.capitalize(), id=f"lang_{lang_name}"))
            checkbox_box.mount(Button("Translate Selected", id="translate_button"))
            self.step = "selection"

        elif event.button.id == "translate_button" and self.step == "selection":
            selected_langs = [
                checkbox.id.replace("lang_", "") for checkbox in checkbox_box.query(Checkbox)
                if checkbox.value
            ]
            print(f"Selected languages: {selected_langs}")
            if not selected_langs:
                output_label.update("Please select at least one language to translate.")
                return
            checkbox_box.query_one("#checkboxLabel").add_class("hidden")
            self.translations = []
            for lang_name, lang_code in self.languages:
                if lang_name in selected_langs:
                    translated = await self.translate(self.targetTranslation, lang_code)
                    self.translations.append(f"{lang_name.capitalize()} ({lang_code}): {translated}")
            output_label.update(
                "Translations:\n" + "\n".join(self.translations) if self.translations else "No translations performed."
            )
            print(f"Translations output: {self.translations}")
            for widget in checkbox_box.query(Checkbox):
                widget.remove()
            checkbox_box.query_one("#translate_button").remove()
            checkbox_box.mount(Button("Quit", id="quit_button"))
            checkbox_box.mount(Button("Save to JSON", id="JSON_button"))
            self.step = "post_translation"

        elif event.button.id == "quit_button" and self.step == "post_translation":
            self.exit()

        elif event.button.id == "JSON_button" and self.step == "post_translation":
            data = {
                "name": self.user_name,
                "age": self.user_age,
                "languages": self.languages,
                "phrase": self.targetTranslation,
                "translations": self.translations,
            }
            with open(f"data{self.user_name}.json", "w") as file:
                json.dump(data, file, indent=4)
            self.exit()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    Kevin_Santos_IO().run()