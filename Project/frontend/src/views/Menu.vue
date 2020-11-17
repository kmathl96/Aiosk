<template>      
      <div class="menu" v-if="getMenu">
        <div style="padding-top: 50px; padding-bottom:0px;">
          <div class="before-cart">
          <div style="display:flex; justify-content:space-between ; margin-bottom:40px;">
            <button @click="moveTotake()" style="margin-left:50px;">
              <font-awesome-icon icon="chevron-left" style="font-size:5em; "/>
              <font-awesome-icon icon="chevron-left" style="font-size:5em; "/>
            </button>
            
            <v-dialog
              v-model="seniormodal"
              max-width="1500"
            >
              <template v-slot:activator="{ on, attrs }" >
                <v-btn
                  dark
                  v-bind="attrs"
                  v-on="on"
                  style="width:200px; height:100px; font-size:2.2em; 
                  border-radius:0.7em; background-color:indianred; margin-right:20px;"
                  @click="yessenior"
                >
                  도움말
                </v-btn>
              </template>
              <v-card style="border-radius:1em;">
                <h1 style="padding-top:10px; margin-bottom:30px; font-size:3em;">
                  도움말
                </h1>
                <div class="col" >
                  <h3 class="text-center" style="font-size:2.0em; margin-bottom:30px;">원하시는 음료를 찾으신 후에 살짝 눌러주세요!</h3>  
                  <h3 class="text-center" style="font-size:2.0em; "><span style="color:#6699cc">주문</span>을 누르고 세부사항을 선택하고 <span style="color:darkorange;">결제</span>나 <span style="color:darkorange;">담기</span>를 눌러주세요!</h3>
                </div>
                <div style="display:flex; justify-content:center; padding-bottom:30px; margin-top:30px;">
                <v-btn style="font-size:2em;" color="red darken-1" text @click="seniormodal = false">닫기</v-btn>
                </div>
              </v-card>
            </v-dialog>
          
          </div>
          <h1 style="font-size:3em; margin-top:50px; margin-bottom:50px;">SMOOTH COFFEE</h1>
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

          <v-tabs
            v-model="tab"
            height="40px"
            class="tab-group"
            slider-color="#6699cc"
            slider-size=4
            centered
            color="#6699cc"
          >
            <!-- <v-tabs-slider></v-tabs-slider> -->
            <v-tab
              class="tab-style"
              v-for="(ch,j) in choice"
              :key="j"
            >
              {{ ch }}
            </v-tab>
          </v-tabs>
            
          <v-dialog
            v-model="showModal"
            persistent
            max-width="80%"
          >
          <template v-slot:activator="{ on, attrs }">
            <v-tabs-items v-model="tab">
            <v-tab-item
              v-for="(ch,j) in choice"
              :key="j"
              height="900px"
            >
            <!-- <div class="menu-container"> -->
              <div class="menu-container">
                <v-card 
                  flat 
                  class="menu-item"
                  v-for="(item,idx) in menus[tab]"
                  @click="setSelected(item)" 
                  :key="idx"
                  v-bind="attrs" 
                  v-on="on"
                >
                  <img
                    :src="require(`@/assets/img/${item.name}.jpg`)"
                    width="250px"
                    height="250px"
                  />
                  <v-card-text class="menu-name">{{item.name}}</v-card-text>
                  <v-card-text class="menu-price">{{item.price}}원</v-card-text>
                </v-card>
              </div>
            <!-- </div> -->
            </v-tab-item>
            </v-tabs-items>
          </template>
          <v-card height="800px"> 
              <div class="modal-body">      
                <img
                 :src="require(`@/assets/img/${selected.name}.jpg`)"
                 width="400px"
                />
                <!-- <img src="@/assets/img/coffee.jpg" style="width:300px;"> -->
                <h1>{{selected.name}}</h1>
                <v-card-text class="modal-text">{{selected.description}}</v-card-text>
                <div class="modal-btn">
                  <v-btn
                    elevation="2"
                    rounded
                    dark
                    height="70px"
                    color="#6699cc"
                    class="btn"
                    @click="moveToOrder"
                  >
                    주문
                  </v-btn>
                  <v-btn
                    elevation="2"
                    rounded
                    height="70px"
                    class="btn"
                    @click="showModal = false"
                  >
                    취소
                  </v-btn>
                </div>
              </div>
          </v-card>
         </v-dialog>
        </div>
        <Cart></Cart>
        </div>
      </div>
</template>

<script>
import axios from 'axios';
import Cart from './Cart'
export default {
name: "Menu",
  components: {Cart},
  data() {
      return {
          publicPath: process.env.BASE_URL,
          menuobject:['포장/주문', '메뉴선택', '추가사항', '결제하기', '완료'],
          choice: ['AI 추천', '커피', '프라페','과일 음료','티','기타 음료'],
          showModal:false,
          phoneNumber: '',
          age:'',
          tab:null,
          step:2,
          selected:{
            name:'에스프레소'
          },
          senior:true,
          seniormodal:false,
          menus:{
            '0':[],
            '1':[],
            '2':[],
            '3':[],
            '4':[],
            '5':[]
          },
          items:[],
          cnt:0,
          cartShow:false,
          getMenu: false,
      }
  },
  created(){
    this.senior=this.$store.getters.getSenior;
    this.seniormodal=this.$store.getters.getSeniorModal;
    if (this.senior == true && this.seniormodal == true){
      this.seniormodal = true
    }
    else {
      this.seniormodal = false
    }
    this.phoneNumber=this.$store.getters.getPhoneNumber;
    this.age=this.$store.getters.getAge;
    axios.get(this.$SERVER_URL+"kiosks/menu_list/")
        .then(res => {
          console.log(res.data)
          res.data.forEach(data=>{
            var idx=data.category;
            if(1<=idx && idx <=5){
              this.menus[idx].push(data)
            }
          });
        })
        .catch(err => {
          console.log(err.message)
        })
    this.cnt=this.$store.getters.getCart.length;
    axios.post(this.$SERVER_URL+"kiosks/recommend/", { 'phone_number': this.phoneNumber, 'age':this.age })
      .then(res => {
        console.log(res)
        res.data.forEach(data=>{
          this.menus[0].push(data)
          this.getMenu=true
        })
      })
      .catch(err => {
        console.log(err)
      })  
  },
  watch:{
      cnt:function(value){
        if(value>0){
          this.cartShow=true;
        }else{
          this.cartShow=false;
        }
      }
  },
  methods: {
    setSelected(item){
      this.selected={...item};
    },
    moveToOrder(){
      this.showModal=false;
      this.$store.commit('setSelected', this.selected);
      this.$router.push({ path: "Order" });
    },
    moveTotake(){
      this.$router.push({path:"Take"})
    },
    yessenior(){
      this.seniormodal = true;
    },
  },
};
</script>


<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
.menu {
  background-color: white;
  min-height: 1700px;
  font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif';
  color:#424242;

}
.menu-container{
  width: 1000px;
  height: 940px;
  padding:10px;
  display:grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 250px 250px;
  grid-gap: 45px;
  margin-top:80px;
  margin-left:auto;
  margin-right:auto;
  margin-bottom: 0px;
}
.menu-item{
  /* width:300px;
  height: 300px;
  margin-right: 50px; */
  /* margin-bottom:60px; */
  display: inline-block;
}
.menu-name{
  font-size:1rem;
  /* color:#2c3e50; */
  font-weight: bold;
  margin-bottom:0px;
  padding:0;
}
.menu-price{
  font-size:1rem;
  /* color:#2c3e50; */
  font-weight: bold;
  margin-bottom:10px;
  padding:0;
}
.modal-body{
  padding-top:100px;
  padding-left:20px;
  padding-right: 20px;
  padding-bottom: 20px;
  margin: 0 auto;
}
.modal-text{
  margin-bottom: 60px;
  font-size: 1.3em;
}
.modal-btn{
  text-align: center;
}
.btn{
  width:300px;
  margin-left: 40px;
  margin-right:40px
}
.btn span{
  font-size:20px;
  font-weight: bold;
}
.tab-group{
  margin-left: auto;
  margin-right: auto;
}
.tab-style{
  width:135px;
  padding-top:10px !important;
  padding-bottom: 15px !important;
  font-size:23px !important;
  font-weight:bold !important;
  margin-left: 10px !important;
  margin-right: 10px;
}
.v-tab{
  display: inline-flex !important;
}
.stepper{
  width: 100%;
  margin-left: auto;
  margin-right:auto;
  margin-bottom:40px;
  box-shadow: none;
}
.v-stepper__label{
  font-size: 1.8em;
  font-weight: 400;
  color:#424242;
}
.before-cart{
  min-height: 65vh;
}
/* .step-header{
  font-size:20px;
  width:20px;
  height: 20px;
  color:#66cccc;
} */
</style>
