import Swal from 'sweetalert2'

const actions = {
  delete ({ dispatch }, payload) {

    Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!',
      timer: 100000,

    }).then((result) => {
      if (result.value) {
        this.$axios.$delete(payload.path)
          .then(() => {
            Swal.fire(
              'Deleted!',
              'Your file has been deleted.',
              'success'
            )
            dispatch(payload.dispatch, { root: true })
          })
      }
    })
  }
}
export default {
  actions
}
