export default {
  path: 'main',
  getComponents(location, cb) {
    require.ensure([], (require) => {
      cb(null, require('./components/Main').default)
    })
  }
};