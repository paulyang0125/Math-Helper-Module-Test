document.getElementById('calculatorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value || 0);
    const operation = document.getElementById('operation').value;
    let result;

    switch (operation) {
        case 'add':
            result = a + b;
            break;
        case 'subtract':
            result = a - b;
            break;
        case 'multiply':
            result = a * b;
            break;
        case 'divide':
            result = b !== 0 ? a / b : 'Error: Division by zero';
            break;
        case 'natural_logarithm':
            result = a > 0 ? Math.log(a) : 'Error: Non-positive value for logarithm';
            break;
        case 'exponential':
            result = Math.exp(a);
            break;
        default:
            result = 'Invalid operation';
    }

    document.getElementById('result').textContent = `Result: ${result}`;
});
