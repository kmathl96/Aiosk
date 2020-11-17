<template>
  <div class="pay">
    <div style="padding-top:20px; padding-bottom:px;">
      <div style="display:flex; justify-content:flex-end ; margin-bottom:100px;">
            
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
                <h1 style="padding-top:20px; margin-bottom:30px; font-size:3em;">
                  도움말
                </h1>
                <div class="col" >
                  <h3 class="text-center" style="font-size:2.0em; margin-bottom:30px;"><span style="color:blue">카드 결제 버튼</span>을 살짝 눌러 파란색이 되면 <span style="color:darkorange;">결제하기</span>를 눌러주세요!</h3>  
                  <h3 class="text-center" style="font-size:2.0em; "><span style="color:#6699cc">주문</span>을 누르고 세부사항을 선택하고 <span style="color:darkorange;">결제</span>나 <span style="color:darkorange;">담기</span>를 눌러주세요!</h3>
                </div>
                <div style="display:flex; justify-content:center; padding-bottom:30px; margin-top:30px;">
                <v-btn style="font-size:2em;" color="red darken-1" text @click="seniormodal = false">닫기</v-btn>
                </div>
              </v-card>
            </v-dialog>
          
          </div>
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
    </div>
    <div style="padding-left:100px; padding-right:100px; padding-top:60px;">
      <div>
  
        <h1 style="text-align:start; margin-top:80px;">결제 방법</h1>
          <div style="display:flex; justify-content:space-around; padding-left:100px; padding-right:100px; margin-top:80px;">          
            <v-dialog
              v-model="capay"
              max-width="700"
            >
              <template v-slot:activator="{ attrs }">
                <button
                  v-if="senior==false"
                  v-bind="attrs"
                  v-bind:class="{active: cardclick}" @click="choicecard"  style="width:200px; height:150px;" 
                >
                  <font-awesome-icon  icon="credit-card" label="카드" style="font-size:5em;"/>
                </button>
                <button
                  v-if="senior==true"
                  v-bind="attrs"
                  class="seniorbutton"
                  v-bind:class="{active: cardclick}" @click="choicecard"  style="width:200px; height:150px;"
                >
                  <h1>카드 결제</h1>
                </button>
              </template>
              <v-card class="text-center" style="border-radius:2em;">
                <h2 style="font-size:3rem; padding-top:10px;">
                  카드 결제를 진행합니다
                </h2>
                <h4 style="margin-top:20px; font-size:1.5rem;">카드를 넣고 결제가 진행되는 동안 빼지 말아주세요.</h4>
                <img src="@/assets/img/card.png" style="width:350px; margin-top:0px;">
                <div style="display:flex; justify-content:center; padding-bottom:50px;">
                <v-btn style="font-size:2rem; margin-right:30px;" color="red darken-1" text @click="capay = false">취소</v-btn>
                <v-btn style="font-size:2rem; margin-left:30px;" color="blue darken-1" text @click="cardpay()">결제</v-btn>
                </div>
              </v-card>
            </v-dialog>
            <v-dialog
              v-model="kapay"
              max-width="600"
            >
              <template v-slot:activator="{ attrs }">
                <button
                  v-if="senior==false"
                  v-bind="attrs"
                  v-bind:class="{active: kakaoclick}" @click="choicekakao"  style="width:200px; height:150px;" 
                >
                  <font-awesome-icon icon="mobile-alt" style="font-size:5em; "/>
                </button>
              </template>
              <v-card style="border-radius:2em;">
                <v-card-title class="headline"  style="display:flex; justify-content:center;">
                  카카오 페이 결제를 진행합니다
                </v-card-title>
                <v-card-text>
                <v-container style="margin-top:10px;">
                    <h1>결제 금액은 {{ final_price }} 원 입니다.</h1>
                </v-container>
              <h4>하단의 결제를 누르시면 카카오 페이로 넘어갑니다</h4>
              </v-card-text>
              <div style="display:flex; justify-content:center; padding-bottom:30px;">
                <v-btn style="font-size:1.5em;" color="red darken-1" text @click="kapay = false">취소</v-btn>
                <v-btn style="font-size:1.5em;" color="blue darken-1" text @click="kakaopay">결제</v-btn>
              </div>
              </v-card>
            </v-dialog>

            <v-dialog
              
              v-model="dialog3"
              max-width="600" 
            >
              <template v-slot:activator="{ on, attrs }">
                <button
                  v-if="senior==false"
                  v-bind="attrs"
                  v-on="on"
                  @click="getCoupons"
                   style="width:200px; height:150px;" 
                >
                  <font-awesome-icon icon="stamp" style="font-size:5em; "/>
                </button>
                <button
                  v-if="senior==true"
                  v-bind="attrs"
                  v-on="on"
                  @click="getCoupons"
                  style="width:200px; height:150px; background-color:#2c3e50; color:white; border-radius:1em;" 
                >
                  <h1>쿠폰 사용</h1>
                </button>
              </template>
              <v-card style="border-radius:2em;">
                <v-card-title class="headline" style="display:flex; justify-content:center;">
                  쿠폰할인
                </v-card-title>
                <v-card-text style="display:flex; justify-content:center;">
                  <v-row>
                    <v-col>
                      <v-checkbox
                        col-12
                        v-model="form.used_coupon"
                        v-for="(item, idx) in coupons"  
                        :key="idx"
                        label="아메리카노 쿠폰"
                        :value="item"
                      ></v-checkbox>
                   </v-col>
                  </v-row>
                </v-card-text>
                <div style="display:flex; justify-content:center; padding-bottom:30px;">
                  <v-btn style="font-size:1.5em;" color="red darken-1" text @click="resetCoupon">취소</v-btn>
                  <v-btn style="font-size:1.5em;" color="blue darken-1" text @click="useCoupon">쿠폰사용</v-btn>
                </div>
              </v-card>
            </v-dialog>
                </div>
              </div>
  



      <div class="container" style="margin-top:80px; margin-left:0px; margin-right:0px;">
        <div class="row">
          <div class="col-7" style="padding:0px;">
            <h1 style="text-align:start;margin-bottom:80px;">결제 메뉴</h1>
               <v-sheet
                elevation="0"
                max-width="1500"
               >
                <v-slide-group
                    style="background-color:white;min-width:900px;"
                    active-class="success"
                    show-arrows
                >
                    <v-slide-item
                    v-for="(item,idx) in menu"
                    :key="idx"
                    v-slot="{ active}"
                    >
                    <v-card
                        color="white"
                        class="pay-card ma-4"
                        height="350"
                        width="250"
                        style="padding-top:20px;margin-left:auto;margin-right:auto"
                    >
                        <div class="pay-content">
                            <img
                                :src="require(`@/assets/img/${item.name}.jpg`)"
                                width="150px"
                                height="150px"
                            />
                            <h2>{{item.name}}</h2> 
                            <h3>수량:{{item.number}}</h3>
                            <h2>
                              <span style="color:#0277BD;margin-right:20px;" v-if="item.type=='ICED'">{{item.type}}</span> 
                              <span style="color:#E53935;margin-right:20px;" v-if="item.type=='HOT'">{{item.type}}</span> 
                            {{item.size}}
                            </h2>
                            <h2 style="color:#FF8F00">{{item.price}} 원</h2>
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
          </div>
        </div>
      </div>
    </div>
    <div class="pay-container">
      <div class="pay-price-container row">
        <div class="col-6" style="text-align:start; padding-top:50px;padding-left:30px;padding-right:30px">
          <h1 style="font-size:30px;margin-bottom:20px;">총 주문 금액</h1>
          <h1 style="margin-bottom:60px;">할인 금액</h1>
          <h1 style="font-size:40px;" id="price">최종 결제 금액</h1>
        </div>
        <div class="col-6" style="text-align:end; padding-top:50px;padding-left:30px;padding-right:30px;">
          <h1 style="font-size:30px;margin-bottom:20px;">{{form.total_price}} 원</h1>
          <h1 style="margin-bottom:60px;">- {{discount}} 원</h1>
          <h1 style="font-size:40px;" id="price">{{ final_price }} 원</h1>
        </div>
      </div>
      <div class="pay-btn-container">
        <v-btn
          dark
          height="80px"
          color="#424242"
          class="pay-fullbtn"
          @click="moveToMenu"
        >
        취소
        </v-btn>
        <v-btn
          dark
          height="80px"
          color="#FF8F00"
          class="pay-fullbtn"
          @click="choicepay"
        >
        결제하기
        </v-btn>
      </div>
    </div>
      <!-- <button id="order" style="margin:50px; width:400px; height:100px;" @click="choicepay"><h3>결제하기</h3></button> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Pay",
  components: {},
  data() {
    return {
      form : {
        menu: {},
        total_price : 0,
        age : '',
        gender : true,
        use_kakao : true,
        used_coupon: [],
        phone_number: ''
      },
      menu: [],
      cart: [],
      menuobject:['포장/주문', '메뉴선택', '추가사항', '결제하기', '완료'],
      dialog3 : false,
      step:4,
      value:'',
      code:'',
      coupons: [],
      cardclick : false,
      kakaoclick: false,
      kapay : false,
      capay : false,
      senior : false,
      seniormodal:false,
      items: ['안녕?'],
      final_price: 0,
      discount: 0,
      use_coupon: false,
      last_coupon_select: []
    }
  },
  watch: {
    dialog3: function(){
      if (this.dialog3 == false){
        this.code = ''
      }
    },
    use_coupon() {
      this.discount = this.form.used_coupon.length * 4100
      this.final_price = this.form.total_price - this.discount
    }
  },
  created(){
    this.getData()
    if (this.senior == true ){
      this.seniormodal = true
    }
    else {
      this.seniormodal = false
    }
  },
  computed: {
  },
  methods: {
      getData() {
        this.menu = this.$store.getters.getPayList
        this.cart = this.$store.getters.getCart
        console.log(this.menu)
        console.log(this.cart)
        this.senior=this.$store.getters.getSenior;
        this.form.menu=this.$store.getters.getPayDict;
        console.log(this.form.menu)
        this.$store.getters.getPayList.forEach(item => {
          this.form.total_price+=item.price
          this.final_price+=item.price
        })
        this.form.phone_number = this.$store.getters.getPhoneNumber
        this.form.age = this.$store.getters.getAge
      },
      getCoupons() {
        axios.post(this.$SERVER_URL+"accounts/coupon/", { phone_number: this.form.phone_number })
          .then(res => {
            this.coupons = res.data.coupon_list
          })
          .catch(err => console.error(err))
      },
       kakaopay(){
            if (this.final_price < 0) {
              alert('결제 금액이 0원보다 적습니다.')
            }
            else {
              this.form.total_price = this.final_price
              axios.post(this.$SERVER_URL+"kiosks/payment/", this.form)
                .then(res => {
                  console.log(res)
                  const payUrl = res.data.next_redirect_pc_url
                  console.log(payUrl)
                  location.href = payUrl
                })
                .catch(err => {
                  console.log(err.message)
                })
            }
        },
        cardpay(){
            if (this.final_price < 0) {
              alert('결제 금액이 0원보다 적습니다.')
            }
            else {
              this.form.total_price = this.final_price
              this.form.use_kakao = false
              axios.post(this.$SERVER_URL+"kiosks/payment/", this.form)
                .then(() => {
                  this.$router.push({path:'Final'});
                })
                .catch(err => {
                  console.log(err.message)
                })
            }
        },
      //   checkcoupon(){
      //     axios.get(this.$SERVER_URL + "accounts/coupon/").then((res) => {
      //       if (res.data.error){
      //         alert(res.data.error+"입니다.")
      //       }
      //       else if (res.data.success){
      //         alert(res.data.success+"했습니다.")
      //       }
      //     }).catch(err=>{
      //       console.log(err)
      //     })
      // },
      resetCoupon() {
        console.log(this.form.used_coupon)
        this.form.used_coupon = this.last_coupon_select
        this.dialog3 = false
      },
      useCoupon() {
        this.use_coupon = !this.use_coupon
        this.last_coupon_select = this.form.used_coupon
        this.dialog3 = false
      },
      choicecard() {
        if (this.cardclick == true){
          this.cardclick = false
        }
        else {
          this.cardclick = true
          this.kakaoclick = false
        }
      },
       choicekakao() {
        if (this.kakaoclick == true){
          this.kakaoclick = false
        }
        else {
          this.kakaoclick = true
          this.cardclick = false
        }
      },
      choicepay(){
        if (this.cardclick == true){
          this.capay = true;
        }
        else if (this.kakaoclick == true){
          this.kapay = true
        }
       else{
         alert('결제방법을 선택해주세요.')
       }
      },
      moveToMenu(){
        this.$router.push({ path: "Menu" });
      },
      yessenior(){
      this.seniormodal = true;
    },
  }
}
</script>


<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
.pay {
  background-color: white;
  height: 1800px;
  font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif';
  color:#424242;
}
.container {
  display:grid;
  margin-top: 200px;
  margin-left:0px;
  margin-right:0px;
  padding-left:0px;
  padding-right:0px;
}
.pay-price-container{
  margin-top:150px;
  /* margin-left:3px; */
  /* margin-right:3px; */
  margin: 0px;
  min-height:350px;
  background-color:#f5f2f0;
}
#price{
  color:orange; 
}
#order{
  background-color:#2c3e50;
  color:white;
  border-radius: 1em;
}
#order:hover{
  background-color: white;
  color: #2c3e50;
  border: 1.4px solid white;
}
.active{
  background-color:#2c3e50;
  color:white;
  border-radius: 1em;
}
input{
  outline:2px solid black;
  width:400px;
  height:50px;
}
.stepper{
  width: 95%;
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
.pay-card{
    display: inline-block !important;
}
.pay-fullbtn{
    display: inline-block;
    width: 50%;
}
.pay-fullbtn span{
    font-size: 40px;
}
.seniorbutton{
  border:3px solid #2c4e50;
  border-radius : 1em;
}
.pay-container {
  position: absolute;
  bottom: 30px;
  width: 100%;
  padding-right: 60px;
  margin-top: 30px;
}
</style>
