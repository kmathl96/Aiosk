<template>
 <div class="cart">
     <div class="cart-container">
        <div class="cart-title">
            <h2 style="display:inline-block;">카트</h2>
            <v-chip
                color="#FF8F00"
                text-color="white"
                height="50px"
            >{{cnt}}</v-chip>
        </div>
        <div class="cart-price">
            <h2 style="display:inline-block;">총 주문 금액 : <span style="color:#FF8F00">{{total}} 원</span> </h2>
        </div>
        <div class="cart-card-container">
            <v-sheet
                class="mx-auto"
                elevation="0"
                max-width="1000"
            >
                <v-slide-group
                    v-model="items"
                    class="cart-slide pa-4"
                    active-class="success"
                    show-arrows
                >
                    <v-slide-item
                    v-for="(item,idx) in items"
                    :key="idx"
                    v-slot="{ active}"
                    >
                    <v-card
                        color="white"
                        class="cart-card ma-4"
                        height="200"
                        width="255"
                    >
                        <div class="card-content">
                        <button class="delete-btn" @click="deleteCart(item.id)">
                                <font-awesome-icon icon="times" style="font-size:1em; "/>
                        </button> 
                            <img
                                :src="require(`@/assets/img/${item.name}.jpg`)"
                                width="80px"
                                height="80px"
                            />
                            <h3>{{item.name}}</h3>
                            <h4>수량:{{item.number}}</h4>
                            <h3 style="color:#FF8F00">{{item.price}}원</h3>
                        </div>
                        <v-row
                        align="center"
                        justify="center"
                        >
                        <v-scale-transition>
                            <v-icon
                            v-if="active"
                            color="white"
                            size="48"
                            v-text="'mdi-close-circle-outline'"
                            ></v-icon>
                        </v-scale-transition>
                        </v-row>
                    </v-card>
                    </v-slide-item>
                </v-slide-group>
            </v-sheet>
            <div class="cart-btn-container" v-if="btnShow===true">
                <v-btn
                 dark
                 height="80px"
                 color="#424242"
                 class="cart-fullbtn"
                >
                취소
                </v-btn>
                <v-btn
                 dark
                 height="80px"
                 color="#FF8F00"
                 class="cart-fullbtn"
                 @click="moveToPay"
                >
                결제하기
                </v-btn>
            </div>
        </div>
     </div>
 </div>  
</template>

<script>
export default {
name: "Cart",
  components: {},
  data() {
      return {
          items:[],
          cnt:'',
          total:0,
          btnShow:false,
      }
  },
  created(){
    this.items=this.$store.getters.getCart;
    this.cnt=this.items.length;
    this.items.forEach(item => {
        this.total+=item.price
    });
 },
  watch:{
      items:function(){
          this.cnt=this.items.length;
          this.total=0;
          this.items.forEach(item => {
            this.total+=item.price
          });
          if(this.cnt>0){
              this.btnShow=true;
          }else {
              this.btnShow=false;
          }
          this.$store.commit('setPayList',this.items);  
      }
  },
  methods: {  
      deleteCart(id){
        this.items=this.items.filter(item=> item.id !=id);
        this.$store.commit('deleteCart',id);
      },
      moveToPay(){
        this.$store.commit('setPayList',this.items); 
        this.$store.commit('setPayDict');
        this.$router.push({ path: "Pay" });
      },
  },
};
</script>

<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
.cart {
  background-color:#f5f2f0;
  width: 100%;
  height: 414px;
  font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif';
  color:#424242;
}
.cart-container{
  position: relative;
}
.cart-title{
    position:absolute;
    top:20px;
    left:40px;
}
.cart-price{
    position:absolute;
    top:20px;
    right:40px;
}
.cart-card-container{
    position:absolute;
    top:70px;
}
.cart-slide{
    background-color:#f5f2f0;
}
.cart-card{
    position: relative;
    display: inline-block !important;
}
.cart-fullbtn{
    display: inline-block !important;
    width:501px;
}
.cart-fullbtn span{
    font-size: 30px;
}
.card-content{
    padding-top:20px;
    padding-left:20px;
    padding-right:20px;
}
.delete-btn{
    position: absolute;
    top:10px;
    right:30px;
}
</style>