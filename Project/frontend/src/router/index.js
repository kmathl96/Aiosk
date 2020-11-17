import Vue from "vue";
import VueRouter from "vue-router";
import Wait from "../views/Wait.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "Home",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Home.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
   {
    path: "/loading",
    name: "Loading",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Loading.vue"),
  },
   {
    path: "/menu",
    name: "Menu",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Menu.vue"),
  },
  {
    path: "/pay",
    name: "Pay",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Pay.vue"),
  },{
    path: "/order",
    name: "Order",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Order.vue"),
  },{
    path: "/",
    name: "Wait",
    component: Wait,
  },
   {
    path: "/final",
    name: "Final",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Final.vue"),
  },
    {
    path: "/member",
    name: "Member",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Member.vue"),
  }, {
    path: "/cart",
    name: "Cart",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Cart.vue"),
  },
    {
    path: "/take",
    name: "Take",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Take.vue"),
  },{
    path: "/class",
    name: "Class",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Class.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
