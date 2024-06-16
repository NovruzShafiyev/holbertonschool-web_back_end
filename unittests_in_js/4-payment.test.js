const { expect } = require('chai');
const Utils = require('./utils');
const sinon = require('sinon');
const sendPaymentRequestToAPI = require('./4-payment');

describe('sendPaymentRequestToAPI', () => {
  let calculateNumberStub;
  let consoleSpy;

  beforeEach(() => {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');
  })

  afterEach(() => {
    calculateNumberStub.restore();
    consoleSpy.restore();
  })

  it('should call Utils.calculateNumber', () => {

    sendPaymentRequestToAPI(100, 20);

    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
  });

  it('should call Utils.calculateNumber only once', () => {

    sendPaymentRequestToAPI(100, 20);

    expect(calculateNumberStub.calledOnce).to.be.true;
  });

  it('should call the console with the correct message', () => {
    sendPaymentRequestToAPI(100, 20);

    expect(consoleSpy.calledWith('The total is: 10'))
  });
});

