function analyzeNutrition() {
    // Get form values
    const form = document.getElementById('nutritionForm');
    const formData = new FormData(form);
    
    // Process form data and perform analysis
    // For demonstration, let's assume some sample analysis based on the answers
    const healthCondition = "Based on your answers, you seem to have a balanced diet.";
    const nutritiousFoods = ["Fruits", "Vegetables", "Whole grains", "Lean protein"];
    const detailedAnalysis = "Your intake of fruits and vegetables seems adequate. However, try to reduce processed foods for better nutrition.";
  
    // Display analysis result
    document.getElementById('healthCondition').textContent = healthCondition;
    const nutritiousFoodsList = document.getElementById('nutritiousFoods');
    nutritiousFoodsList.innerHTML = '';
    nutritiousFoods.forEach(food => {
      const listItem = document.createElement('li');
      listItem.textContent = food;
      nutritiousFoodsList.appendChild(listItem);
    });
    document.getElementById('detailedAnalysis').textContent = detailedAnalysis;
  
    // Show the analysis result section
    document.getElementById('analysisResult').classList.remove('hidden');
  }
  