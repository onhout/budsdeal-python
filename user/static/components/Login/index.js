export default {
  path: 'login',
  getComponents(location, cb) {
    require.ensure([], (require) => {
      cb(null, require('./components/Login').default)
    })
  }
};