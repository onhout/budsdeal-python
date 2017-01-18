export default {
  path: 'signup',
  getComponents(location, cb) {
    require.ensure([], (require) => {
      cb(null, require('./components/Signup').default)
    })
  }
};