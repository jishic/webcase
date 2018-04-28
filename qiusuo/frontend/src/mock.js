const Mock = require('mockjs');
Mock.mock('/backend/login', 'post',{
    'success': true,
    'isTea':true,
    'username':'蒋经国',
    'password':"123",
    'email':'704464080@qq.com',
    'gender':true,
    'telephone':'13075589167',
    'imgUrl': '/static/icon.jpg'}
);
Mock.mock('/backend/register', 'post',{
    'success': true,
    'isTea':true,
    'username':'飘过云追去',
    'password':"123",
    'email':'',
    'gender':true,
    'telephone':'',
    'imgUrl': '/static/head.jpg'}
);
Mock.mock('/backend/attention', 'post',{
    'success': true,
    'list':[{'name':'刘德华','type':1},
            {'name':'张学友','type':1},
            {'name':'吴彦祖','type':1},
            {'name':'成龙','type':0},
            {'name':'梁朝伟','type':0}]}
);
Mock.mock('/backend/requireidentify', 'post',{
    'success': true,}
);
Mock.mock('/backend/requirePass', 'post',{
    'success': true,}
);
Mock.mock('/backend/alterPass', 'post',{
    'success': true,}
);
Mock.mock('/backend/LiveList', 'post',{
    'success': true,
    'list':[{'title':'c++学堂','username':'王教授'},
            {'title':'c++学堂','username':'王教授'},
            {'title':'c++学堂','username':'王教授'},
            {'title':'c++学堂','username':'王教授'},
            {'title':'c++学堂','username':'王教授'}]}
);

Mock.mock('/backend/focuslist', 'post',{
    'success': true,
    'list':[{'teachername':'王教授'},
            {'teachername':'王教授'},
            {'teachername':'王教授'},
            {'teachername':'王教授'},
            {'teachername':'王教授'},]}
);