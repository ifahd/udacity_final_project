import Vue from 'vue'
import { mapGetters } from 'vuex'

const permissions = {
  install (Vue, options) {
    Vue.mixin({
      computed: {
        ...mapGetters({
          permissions: 'permissions/permissions'
        })
      }
    })
  }
}

Vue.use(permissions)
