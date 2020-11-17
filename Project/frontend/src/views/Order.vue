<template>    
    <div class="order">
        <div style="padding-top: 10px; padding-bottom:0px;">
             <h1 style="font-size: 3em; margin-bottom:40px">SMOOTH COFFEE</h1>
            <v-stepper 
                class="stepper"
                alt-labels 
                v-model="step"
            >
                <v-stepper-header class="step-header">
                    <div
                        v-for="index in 5"  
                        :key="index"
                    >
                        <v-stepper-step
                        :complete="step>index"
                        :step="index"
                        color="#FF8F00"
                        >
                        {{menuobject[index-1]}}
                        </v-stepper-step>
                    </div> 
                </v-stepper-header>
            </v-stepper>
        
        <div class="order-container">
        <button class="back-btn" @click="moveToMenu()">
            <font-awesome-icon icon="chevron-left" style="font-size:3em; "/>
        </button>
        <img
        :src="require(`@/assets/img/${item.name}.jpg`)" 
         style="padding-top:120px;width:400px; margin-top:0px;margin-bottom:30px">
        <h1 style="color:#424242">{{item.name}}</h1>
        <h1 style="color:#424242">{{item.price}} 원</h1>
            <div class="btn-container">
                <v-btn
                    rounded
                    dark
                    height="70px"
                    color="#6699cc"
                    class="number-btn"
                    @click="subNumber"
                >-</v-btn>
                <v-text-field
                rounded
                outlined
                dense
                color="#6699cc"
                class="number-text"
                height="70px"
                readonly
                v-model="number"
                ></v-text-field>
                <v-btn
                    rounded
                    dark
                    height="70px"
                    color="#6699cc"
                    class="number-btn"
                    @click="addNumber"
                >+</v-btn>
            </div>
            <v-chip-group
                v-if="item.category===1 || item.category===4 || item.category===5"
                mandatory
                class="type-chip-group"
                v-model="type"
                active-class="selected"
            >
                    <v-chip
                        v-if="type=='ICED'"
                        color="#6699cc"
                        text-color="white"
                        height="100px"
                        class="type-chip"
                        x-large
                        value="ICED"
                        style="margin-right:40px;"
                    >ICED</v-chip>
                    <v-chip
                        v-if="type!='ICED'"
                        color="#6699cc"
                        outlined
                        height="100px"
                        class="type-chip"
                        x-large
                        value="ICED"
                        style="margin-right:40px;"
                    >ICED</v-chip>
                    <v-chip
                        v-if="type=='HOT'"
                        color="#6699cc"
                        text-color="white"
                        height="100px"
                        class="type-chip"
                        x-large
                        value="HOT"
                    >HOT</v-chip>
                    <v-chip
                        v-if="type!='HOT'"
                        color="#6699cc"
                        outlined
                        height="100px"
                        class="type-chip"
                        x-large
                        value="HOT"
                    >HOT</v-chip>
            </v-chip-group>
                <v-chip-group
                mandatory
                class="size-chip-group"
                v-model="size"
                active-class="selected"
            >
                    <template
                        v-for="(s,idx) in sizes"
                    >
                        <v-chip
                        v-if="size===s"
                        color="#6699cc"
                        text-color="white"
                        height="100px"
                        class="size-chip"
                        x-large
                        :value="s"
                        :key="idx"
                        style="margin-right:15px;"
                        >{{s}}</v-chip>
                    <v-chip
                        v-if="size!==s"
                        color="#6699cc"
                        outlined
                        height="100px"
                        class="size-chip"
                        x-large
                        :value="s"
                        :key="idx"
                        style="margin-right:15px;"
                    >{{s}}</v-chip>
                    </template>
            </v-chip-group>
            <div class="fullbtn-container">
                <v-btn 
                    dark
                    height="70px"
                    color="#FF8F00"
                    class="fullbtn"
                    @click="moveToPay"
                >결제</v-btn>
                <v-btn 
                    outlined
                    height="70px"
                    color="#FF8F00"
                    class="fullbtn"
                    @click="addCart"
                >담기</v-btn>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Order",
  components: {},
  data() {
    return {
        item:{},
        menuobject:['포장/주문', '메뉴선택', '추가사항', '결제하기', '완료'],
        type:'ICED',
        size:'LARGE',
        price:'',
        sizes:['SMALL','LARGE','EXTRA'],
        number:1,
        step:3,
        seniormodal:false,
    }
  },
  created(){
    this.item={...this.$store.getters.getSelected};
    this.item.number=1;
    this.item.type='ICED';
    this.item.size='LARGE';
    this.price=this.item.price;
    console.log(this.item)
  },
watch:{
    size:function(value){
          if(value==='SMALL'){
              this.item.price=(this.price-500)*this.number;
          }else if(value==='EXTRA'){
              this.item.price=(this.price+500)*this.number;
          }else if(value==='LARGE'){
              this.item.price=this.price*this.number;
          }
      },
      number:function(value){
          if(this.size==='SMALL'){
              this.item.price=(this.price-500)*value;
          }else if(this.size==='EXTRA'){
              this.item.price=(this.price+500)*value;
          }else if(this.size==='LARGE'){
              this.item.price=this.price*value;
          }
      }

  },
  methods: {
      addNumber(){
          this.number+=1;
      },
      subNumber(){
          if(this.number>1){
              this.number-=1;
          }
      },
      moveToPay(){
        let order={...this.item,"size":this.size,"type":this.type,"number":this.number}
        this.$store.commit("addCart",order);
        this.$store.commit('addPayList',this.item);
        this.$store.commit('setPayDict');
        this.$store.commit('seniorModal',this.seniormodal)
        this.$router.push({ path: "Pay" });
      },
      addCart(){
          let order={...this.item,"size":this.size,"type":this.type,"number":this.number}
          this.$store.commit("addCart",order);
          this.$store.commit('seniorModal',this.seniormodal)
          this.$router.push({ path: "Menu" });
      },
      moveToMenu(){
        this.$router.push({ path: "Menu" });
      }
  },
};
</script>


<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
.order {
  background-color: white;
  height: 1800px;
  font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif';
  color:#424242;
}
.order-container{
   position: relative;
   margin-top:70px;
   padding-top:100px;
   margin-left: auto;
   margin-right:auto;
   border-radius: 40px;
   box-shadow: 0px -40px 30px -30px #BDBDBD;
}
.back-btn{
    color:#424242;
    position: absolute;
    top:50px;
    left: 50px;
}
.btn-container{
   margin-top:50px;  
}
.stepper{
  width: 100%;
  margin-left: auto;
  margin-right:auto;
  margin-bottom:30px;
  box-shadow: none;
}
.v-stepper__label{
  font-size: 1.8em;
  font-weight: 400;
  color:#424242;
}
.v-slide-group__content{
    display: block !important;
}
.fullbtn-container{
    margin-top:100px;
    text-align:center;
}
.fullbtn{
    width: 350px;
    margin-right:25px;
}
.fullbtn span{
    font-size: 35px;
}
.number-btn{
  padding:0;
  width:120px;
  margin-left: 25px;
  margin-right:25px
}
.number-btn span{
    font-size: 40px;
    font-weight: bold;
}
.number-text{
    display: inline-block !important;
    width:350px;
    padding:0px;
}
.number-text input{
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    color: #6699cc;
}
.type-chip-group,.size-chip-group{
    margin-bottom: 20px;
}
.selected{
    background-color: white;
    border-color: #6699cc;
}
.type-chip{
    width: 300px;
}
.size-chip{
    width: 200px;
}
.size-chip span{
    font-weight: bold;
}
.type-chip span{
    font-weight: bold;
    display: inline-block;
    text-align: center;
}
.v-chip__content{
    margin-left: auto;
    margin-right: auto;
}
</style>
