<template>
<div class="container">
  <div>
    <Logo />
    <h1 class="title">
      Casting Agency
    </h1>
    <p>The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies</p>
    <template v-if="$auth.loggedIn">
      <p><b>Your Access Token:</b></p>
      <p style="word-break: break-all;">{{ token }}</p>
    </template>
  </div>
</div>
</template>

<script>
export default {
  auth: 'guest',
  computed: {
    token() {
      if(process.browser){
        if(localStorage.getItem('auth._token.auth0') !== undefined && localStorage.getItem('auth._token.auth0') !== null) {
          return localStorage.getItem('auth._token.auth0').replace('Bearer ', '')
        }
      }
    }
  },
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
