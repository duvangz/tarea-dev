from typing import List, Tuple, Dict


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución
    
    return 0


def run_tests() -> None:
    test_cases: List[Dict[str, int]] = [
        {"panel_w": 1, "panel_h": 2, "roof_w": 2, "roof_h": 4, "expected": 4},
        {"panel_w": 1, "panel_h": 2, "roof_w": 3, "roof_h": 5, "expected": 7},
        {"panel_w": 2, "panel_h": 2, "roof_w": 1, "roof_h": 10, "expected": 0}
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
    
    # Run test cases
    run_tests()


if __name__ == "__main__":
    main()
