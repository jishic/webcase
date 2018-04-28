import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
const state = {
    messages:[]
}
const mutations={
    onNewMessage(state,msg) { 
        state.messages.push(msg)
    }
}
const actions={
    onNewMessage({commit},data) {
        setTimeout( () => {
          commit('onNewMessage',data)
        },10)
    }
}
export default new Vuex.Store({
    state,
    mutations,
    actions
});
