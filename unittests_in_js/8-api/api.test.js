const {expect} = require('chai');
const request = require('request');

describe('API route /', function() {
  it('should send the correct status code', function(done) {
    request.get('http://localhost:7865', (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    })
  });

  it('should send the correct result', function(done) {
    request.get('http://localhost:7865', (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    })
  })
});
