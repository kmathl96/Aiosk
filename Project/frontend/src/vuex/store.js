import Vue from "vue";
import Vuex from "vuex";

import getters from './getters'
import actions from './actions'
import mutations from './mutations'

Vue.use(Vuex)

const state = {
    selected:{},
    cart:[],
    phoneNumber:'',
    payList:[],
    payDict: {},
    senior: true,
    seniormodal: true,
    age: '',
    letter: '',
}

export default new Vuex.Store({
    state,
    mutations,
    getters,
    actions
})
