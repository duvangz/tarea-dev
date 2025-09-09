from typing import List, Tuple, Dict
import json
from math import floor

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    def mix_x():
        best = 0
        for k in range(0, floor(roof_width / panel_width) + 1):
            n = k * floor(roof_height / panel_height) + floor((roof_width - k * panel_width) / panel_height) * floor(roof_height / panel_width)
            if (n > best):
                best = n

        return best
    
    def mix_y():
        best = 0
        for k in range(0, floor(roof_height / panel_height)):
            n = k * floor(roof_width / panel_width) + floor((roof_height - k * panel_height) / panel_width) * floor(roof_width / panel_height)
            if ( n > best):
                best = n

        return best

    return max(mix_x(), mix_y())

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
