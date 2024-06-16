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

describe('API route /:id', function() {
  it('should send the correct status code when id is a number', function (done) {
    request.get('http://localhost:7865/cart/1', (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should send a 404 status code when id is not a number', function(done) {
    request.get('http://localhost:7865/cart/o', (error, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should send the correct message', function(done) {
    request.get('http://localhost:7865/cart/1', (err, res, body) => {
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  })
});


  describe('API route /login', function() {
    it('should send the correct status code and message', function(done) {
      const req = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: true,
        body: {
          userName: "Moustapha"
        }
      };

      request.post(req, (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Moustapha');
        done();
      });
    });
  });

  describe('API route /available_payments', function() {
    it('send the correct message', function(done) {
      request.get('http://localhost:7865/available_payments', (error, response, body) => {
        const res = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        };
        expect(JSON.parse(body)).to.deep.equal(res);
        done();
      });
    });
});
