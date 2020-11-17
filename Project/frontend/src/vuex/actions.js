export default {
    setSelected:function(context,payload){
      if(payload!=null){
        context.commit("setSelected",payload);
      }
    },
    addCart:function(context,payload){
        if(payload!=null){
            context.commit("addCart",payload);
        }
    },
    deleteCart:function(context,payload){
        if(payload!=null){
            context.commit("deleteCart",payload);
        }
    },
    setPhoneNumber:function(context,payload){
        if(payload!=null){
            context.commit("setPhoneNumber",payload);
        }
    },
    setPayList:function(context,payload){
        if(payload!=null){
            context.commit("setPayList",payload);
        }
    },
    addPayList:function(context,payload){
        if(payload!=null){
            context.commit('addPayList',payload);
        }
    },
    seniorModal: function (context, payload) {
        context.commit("seniorModal", payload)
    },
    reset:function(context){
        context.commit('reset');
    }
        
}
