import Vue from 'vue'
import Router from 'vue-router'
import lifeStreem from '../components/lifeStreem'
import PersonalDate from '@/components/PersonalDate'
import FocusList from '@/components/FocusList'
import ChangePassword from '@/components/ChangePassword'
import room from '../components/room'
import ApplyLive from '@/components/ApplyLive'
import studio from '@/components/studio'

import student from '@/components/student'

import forgetPass from '@/components/forgetPass'
import aaaa from '@/components/aaaa'


Vue.use(Router)

export default new Router({
	routes: [
	{
		path: '/',
		name: 'lifestreem',
		component: lifeStreem
	},
	{
		path: '/focusList',
		name: 'FocusList',
		component: FocusList
	},
     {
      path: '/ChangePassword',
      name: 'ChangePassword',
      component: ChangePassword

    },
    {
    	path: '/PersonalDate',
    	name: 'PersonalDate',
    	component: PersonalDate
    },
    {
    	path: '/room',
    	name: 'room',
    	component: room
    },
    {
        path: '/ApplyLive',
        name: 'ApplyLive',
        component: ApplyLive
    },
    {
        path: '/studio',
        name: 'studio',
        component: studio
    },

    {
        path: '/student',
        name: 'student',
        component: student
    },
    {
        path: '/forgetPass',
        name: 'forgetPass',
        component: forgetPass
    },
    {
        path: '/aaaa',
        name: 'aaaa',
        component: aaaa
    },

    ]
})
