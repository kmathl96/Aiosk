import Vue from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faMugHot, faSignOutAlt, faBackspace, faTicketAlt, faCoffee, faStamp, faMobileAlt, faCreditCard, faLink, faRedo, faUndo, faChevronLeft,faTimes } from "@fortawesome/free-solid-svg-icons";
import { faTrashAlt } from "@fortawesome/free-regular-svg-icons";

library.add( faTrashAlt);
library.add( faMugHot, faSignOutAlt, faBackspace, faTicketAlt, faCoffee, faStamp, faMobileAlt, faCreditCard, faLink, faRedo, faUndo,faChevronLeft,faTimes);

Vue.component('font-awesome-icon', FontAwesomeIcon)