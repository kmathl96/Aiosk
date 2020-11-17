export default {
    setSelected:function(state,payload){
        state.selected={...payload};
    },
    addCart:function(state,payload){
        console.log(payload.number)
        console.log(state.cart)
        if (state.cart.length === 0) {
            state.cart.push(payload)
        }
        else{
            for (let i in state.cart) {
                console.log("I: ", i, "length : ", state.cart.length - 1 )
                if (state.cart[i].name === payload.name && state.cart[i].size === payload.size && state.cart[i].type === payload.type) {
                    state.cart[i].number += payload.number
                    state.cart[i].price += payload.price
                    break;
                }
                else if (Number(i) === (state.cart.length - 1)){
                    state.cart.push(payload);
                }
            }
        }
    },
    deleteCart:function(state,payload){
        state.cart=state.cart.filter(item=> item.id !=payload);
    },
    setAge:function(state,payload){
        state.age=payload;
        if (payload === 'senior') {
            state.senior = true
        }
        else {
            state.senior = false
        }
    },
    setPhoneNumber:function(state,payload){
        let result = '';
        for (let letter of payload) {
            if (letter !==' ' && letter !== '-')
                result += letter;
        }
        state.phoneNumber=result;
    },
    setPayDict:function(state){
        let items = {}
        for (let i in state.cart) {
            items[state.payList[i]['name']] = state.payList[i]['number']
        }
        state.payDict = items
    },
    setPayList:function(state,payload){
        state.payList = payload.slice()
    },
    addPayList:function(state,payload){
        state.payList.push(payload)
    },
    seniorModal: function (state, payload) {
        state.seniormodal = payload
    },
    reset:function(state){
        state.selected={},
        state.cart=[],
        state.phoneNumber='',
        state.payList=[],
        state.payDict=[],
        state.age='',
        state.senior=true,
        state.letter=''
    },
    setLetter: function(state, payload) {
        state.letter = payload
    }
}

