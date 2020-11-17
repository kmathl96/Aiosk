export default {
   getSelected:function(state){
       return state.selected;
   },
   getCart:function(state){
       return state.cart;
   },
   getPhoneNumber:function(state){
       return state.phoneNumber;
   },
   getAge:function(state){
       return state.age;
   },
   getPayList:function(state){
       return state.payList;
   },
   getSenior: function (state) {
        return state.senior;
    },
    getSeniorModal: function (state) {
        return state.seniormodal;
   },
   getPayDict: function(state) {
       return state.payDict;
   },
   getLetter: function(state) {
       return state.letter;
   }
}