const { expect } = require('chai');
const Utils = require('./utils');
const sinon = require('sinon');
const sendPaymentRequestToAPI = require('./3-payment');

describe('sendPaymentRequestToAPI', () => {
  let calculateNumberSpy;

  beforeEach(() => {
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  })

  afterEach(() => {
    calculateNumberSpy.restore();
  })

  it('should call Utils.calculateNumber', () => {

    sendPaymentRequestToAPI(1, 2);

    expect(calculateNumberSpy.calledWith('SUM', 1, 2)).to.be.true;
  });

  it('should call Utils.calculateNumber only once', () => {

    sendPaymentRequestToAPI(1, 2);

    expect(calculateNumberSpy.calledOnce).to.be.true;
  })
});

