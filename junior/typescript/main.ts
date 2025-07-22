function calculatePanels(
  panelWidth: number,
  panelHeight: number,
  roofWidth: number,
  roofHeight: number
): number {
  // Implementa acá tu solución
  
  return 0;
}

function main(): void {
  console.log("🐕 Wuuf wuuf wuuf 🐕");
  console.log("================================\n");
  
  runTests();
}

function runTests(): void {
  const testCases = [
    { panelW: 1, panelH: 2, roofW: 2, roofH: 4, expected: 4 },
    { panelW: 1, panelH: 2, roofW: 3, roofH: 5, expected: 7 },
    { panelW: 2, panelH: 2, roofW: 1, roofH: 10, expected: 0 }
  ];
  
  console.log("Corriendo tests:");
  console.log("-------------------");
  
  testCases.forEach((test, index) => {
    const result = calculatePanels(test.panelW, test.panelH, test.roofW, test.roofH);
    const passed = result === test.expected;
    
    console.log(`Test ${index + 1}:`);
    console.log(`  Panels: ${test.panelW}x${test.panelH}, Roof: ${test.roofW}x${test.roofH}`);
    console.log(`  Expected: ${test.expected}, Got: ${result}`);
    console.log(`  Status: ${passed ? "✅ PASSED" : "❌ FAILED"}\n`);
  });
}

main();
