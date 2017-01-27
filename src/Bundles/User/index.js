export default {
    path: 'user',
      getChildRoutes(partialNextState, cb) {
      require.ensure([], (require) => {
        cb(null, [
          require('./components/Login').default,
          require('./components/Signup').default,
        ])
      })
    },

    getComponents(location, cb) {
        require.ensure([], (require) => {
            cb(null, require('./components/User').default)
        })
    }
};