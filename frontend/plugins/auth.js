export default function ({ app, $auth, env }) {
  if ($auth.loggedIn) {
    app.$axios.$get('https://api-final-project-fahd.herokuapp.com/permissions')
    .then((response) => {
      app.store.dispatch('permissions/setPermissions',response.permissions)
    })
  }
}

