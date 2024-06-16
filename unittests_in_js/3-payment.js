const Utils = require('./utils');

module.exports = function sendPaymentRequestToAPI(totalAmount, totalShipping) {
  console.log(`The total is: ${Utils.calculateNumber('SUM', totalAmount, totalShipping)}`);
};
