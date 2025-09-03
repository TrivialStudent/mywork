import shapes
import utils
from day_03.modular_code.ShapeToolkit.utils import compareTwoShapes

bob = shapes.Rectangle(3, 7)
siddiqi = shapes.Circle(5)

if __name__ == "__main__":
    print(f"bob has area {bob.area}, and siddiqi has area {siddiqi.area}")

    compareTwoShapes(bob,siddiqi)