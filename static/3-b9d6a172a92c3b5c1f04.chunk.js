webpackJsonp([3],{

/***/ 599:
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	
	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();
	
	var _react = __webpack_require__(85);
	
	var _react2 = _interopRequireDefault(_react);
	
	var _Button = __webpack_require__(600);
	
	var _Button2 = _interopRequireDefault(_Button);
	
	var _Button3 = __webpack_require__(601);
	
	var _Button4 = _interopRequireDefault(_Button3);
	
	var _reactBootstrap = __webpack_require__(342);
	
	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }
	
	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
	
	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }
	
	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }
	
	var Login = function (_React$Component) {
	    _inherits(Login, _React$Component);
	
	    function Login(props) {
	        _classCallCheck(this, Login);
	
	        var _this = _possibleConstructorReturn(this, (Login.__proto__ || Object.getPrototypeOf(Login)).call(this, props));
	
	        _this.state = {
	            email: '',
	            password: ''
	        };
	        _this.handleValidation = _this.handleValidation.bind(_this);
	        //React components using ES6 classes no longer autobind this to non React methods
	        //http://www.newmediacampaigns.com/blog/refactoring-react-components-to-es6-classes
	        return _this;
	    }
	
	    _createClass(Login, [{
	        key: 'getValidationState',
	        value: function getValidationState(input) {
	            // regex from http://stackoverflow.com/questions/46155/validate-email-address-in-javascript
	            var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	            var bool = re.test(input);
	            if (bool) return 'success';else return 'error';
	        }
	    }, {
	        key: 'handleValidation',
	        value: function handleValidation(e) {
	            this.setState({
	                email: e.target.value
	            });
	        }
	    }, {
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                _reactBootstrap.Col,
	                { xs: 12, md: 8, mdOffset: 2 },
	                _react2.default.createElement(
	                    _reactBootstrap.Form,
	                    null,
	                    _react2.default.createElement(
	                        _reactBootstrap.FormGroup,
	                        {
	                            controlId: 'email',
	                            validationState: this.getValidationState(this.state.email),
	                            bsSize: 'lg'
	                        },
	                        _react2.default.createElement(
	                            _reactBootstrap.ControlLabel,
	                            null,
	                            'Username'
	                        ),
	                        _react2.default.createElement(_reactBootstrap.FormControl, {
	                            type: 'email',
	                            value: this.state.email,
	                            placeholder: 'Enter email',
	                            onChange: this.handleValidation
	                        }),
	                        _react2.default.createElement(_reactBootstrap.FormControl.Feedback, null),
	                        _react2.default.createElement(
	                            _reactBootstrap.HelpBlock,
	                            null,
	                            'Your username is usually your email address'
	                        )
	                    ),
	                    _react2.default.createElement(
	                        _reactBootstrap.FormGroup,
	                        {
	                            controlId: 'password',
	                            bsSize: 'lg'
	                        },
	                        _react2.default.createElement(
	                            _reactBootstrap.ControlLabel,
	                            null,
	                            'Password'
	                        ),
	                        _react2.default.createElement(_reactBootstrap.FormControl, {
	                            type: 'password',
	                            value: this.state.password,
	                            placeholder: 'Enter password'
	                        }),
	                        _react2.default.createElement(_reactBootstrap.FormControl.Feedback, null)
	                    ),
	                    _react2.default.createElement(
	                        _reactBootstrap.FormGroup,
	                        { className: 'pull-right' },
	                        _react2.default.createElement(
	                            _reactBootstrap.Button,
	                            { type: 'submit', bsSize: 'lg' },
	                            'Sign in'
	                        )
	                    ),
	                    _react2.default.createElement(_Button2.default, null),
	                    _react2.default.createElement(
	                        'div',
	                        { style: { marginTop: 10 } },
	                        _react2.default.createElement(_Button4.default, null)
	                    )
	                )
	            );
	        }
	    }]);
	
	    return Login;
	}(_react2.default.Component);
	
	exports.default = Login;

/***/ },

/***/ 600:
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	
	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();
	
	var _react = __webpack_require__(85);
	
	var _react2 = _interopRequireDefault(_react);
	
	var _reactBootstrap = __webpack_require__(342);
	
	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }
	
	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
	
	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }
	
	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }
	
	var FacebookButton = function (_React$Component) {
	    _inherits(FacebookButton, _React$Component);
	
	    function FacebookButton() {
	        _classCallCheck(this, FacebookButton);
	
	        return _possibleConstructorReturn(this, (FacebookButton.__proto__ || Object.getPrototypeOf(FacebookButton)).apply(this, arguments));
	    }
	
	    _createClass(FacebookButton, [{
	        key: 'logIn',
	        value: function logIn() {
	            alert('Log in or register');
	        }
	    }, {
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    _reactBootstrap.Button,
	                    { bsStyle: 'primary', onClick: this.logIn, bsSize: 'lg', block: true },
	                    _react2.default.createElement('i', { className: 'fa fa-facebook-official' }),
	                    ' Facebook Login'
	                )
	            );
	        }
	    }]);
	
	    return FacebookButton;
	}(_react2.default.Component);
	
	exports.default = FacebookButton;

/***/ },

/***/ 601:
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	
	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();
	
	var _react = __webpack_require__(85);
	
	var _react2 = _interopRequireDefault(_react);
	
	var _reactBootstrap = __webpack_require__(342);
	
	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }
	
	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
	
	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }
	
	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }
	
	var GoogleButton = function (_React$Component) {
	    _inherits(GoogleButton, _React$Component);
	
	    function GoogleButton() {
	        _classCallCheck(this, GoogleButton);
	
	        return _possibleConstructorReturn(this, (GoogleButton.__proto__ || Object.getPrototypeOf(GoogleButton)).apply(this, arguments));
	    }
	
	    _createClass(GoogleButton, [{
	        key: 'logIn',
	        value: function logIn() {
	            alert('Log in or register');
	        }
	    }, {
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    _reactBootstrap.Button,
	                    { bsStyle: 'danger', onClick: this.logIn, bsSize: 'lg', block: true },
	                    _react2.default.createElement('i', { className: 'fa fa-google-plus' }),
	                    ' Google+ Login'
	                )
	            );
	        }
	    }]);
	
	    return GoogleButton;
	}(_react2.default.Component);
	
	exports.default = GoogleButton;

/***/ }

});
//# sourceMappingURL=3-b9d6a172a92c3b5c1f04.chunk.js.map