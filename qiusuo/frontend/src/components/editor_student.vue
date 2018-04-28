<template>
    <div>
        <editor v-model="content" @init="editorInit" lang="html" theme="monokai" width="800" height="600"></editor>
    </div>
</template>

<script>
export default{
    components: {
        editor: require('vue2-ace-editor')
    },
    data() {
        return {
            content:""
        }
    },
    mounted() {
        this.collert();
    },
    methods: {
        editorInit: function () {
            require('../../node_modules/brace/mode/html')
            require('../../node_modules/brace/mode/javascript')
            require('../../node_modules/brace/mode/less')
            require('../../node_modules/brace/theme/monokai')
        },
        collert(){
            var vm = this;
            var signal = Signal("e0c9a73631634507b07b18b5263d129f");
            var session = signal.login("wwk2", "_no_need_token");
            session.onLoginSuccess = function(uid){

                var channel = session.channelJoin("111");
                channel.onChannelJoined = function(){
                    channel.onMessageChannelReceive = function(account, uid, msg){
                        vm.content = msg;
                    }

                };
            };
        },
    }
}
</script>

<style scoped>

</style>
