module.exports = {
  calculateNumber(type, a, b) {
    const x = Math.round(a);
    const y = Math.round(b);

    switch (type) {
      case 'SUM':
        return x + y;
      case 'SUBTRACT':
        return x - y;
      case 'DIVIDE': {
        if (y === 0) {
          return 'Error';
        }
        return x / y;
      }
      default:
        return 'Error';
    }
  },
};
