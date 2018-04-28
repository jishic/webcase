
<template>
<div>
<div  style="display: none;">
<div id="div_device" class="panel panel-default">
<div class="select">
<label for="audioSource">Audio source: </label><select id="audioSource"></select>
</div>
<div class="select">
<label for="videoSource">Video source: </label><select id="videoSource"></select>
</div>
</div>
</div>

<div id="div_join" class="panel panel-default">
<div class="panel-body" style="display: none;">
<input id="video" type="checkbox"   ></input>
</div>
</div>



<div id="video" style="margin:0 auto;">
    <button id="join"  class="camera-btn" @click="join" v-show="!cameraon">加入</button>
    <div id="agora_local" style="width:300px;height:200px;"></div>
</div>
 </div>
 
</template>
 
<script>
import {AgoraRTC} from "../AgoraRTCSDK-2.1.1"
import {jQuery} from "../vendor/jquery"


export default {
    data () {
    return {
        channel:"1000",
        cameraon:false
    }
    },
    created(){
        this.join()
    },
    methods:{
    join() {
        
        var keyValue='dab77282fe784dc085c411ee19f34422';
        var channelValue=this.channel;
        var audioSelect = document.querySelector('select#audioSource');
        var videoSelect = document.querySelector('select#videoSource');
        var client, localStream, camera, microphone;
        document.getElementById("join").disabled = true;
        document.getElementById("video").disabled = true;
        var channel_key = null;

        console.log("Init AgoraRTC client with vendor key: " + keyValue);
        client = AgoraRTC.createClient({mode: 'interop'});
        client.init(keyValue, function () {
            console.log("AgoraRTC client initialized");
            client.join(channel_key, channelValue, null, function(uid) {
            console.log("User " + uid + " join channel successfully");

            if (document.getElementById("video").checked) {
                camera = videoSource.value;
                microphone = audioSource.value;
                localStream = AgoraRTC.createStream({streamID: uid, audio: true, cameraId: camera, microphoneId: microphone, video: document.getElementById("video").checked, screen: false});
                //localStream = AgoraRTC.createStream({streamID: uid, audio: false, cameraId: camera, microphoneId: microphone, video: false, screen: true, extensionId: 'minllpmhdgpndnkomcoccfekfegnlikg'});
                if (document.getElementById("video").checked) {
                localStream.setVideoProfile('720p_3');
                
                }

                // The user has granted access to the camera and mic.
                localStream.on("accessAllowed", function() {
                console.log("accessAllowed");
                });

                // The user has denied access to the camera and mic.
                localStream.on("accessDenied", function() {
                console.log("accessDenied");
                });

                localStream.init(function() {
                console.log("getUserMedia successfully");
                localStream.play('agora_local');

                client.publish(localStream, function (err) {
                    console.log("Publish local stream error: " + err);
                });

                client.on('stream-published', function (evt) {
                    console.log("Publish local stream successfully");
                });
                }, function (err) {
                console.log("getUserMedia failed", err);
                });
            }
            }, function(err) {
            console.log("Join channel failed", err);
            });
        }, function (err) {
            console.log("AgoraRTC client init failed", err);
        });
        this.cameraon=true;
        var  channelKey = "";
        client.on('error', function(err) {
            console.log("Got error msg:", err.reason);
            if (err.reason === 'DYNAMIC_KEY_TIMEOUT') {
            client.renewChannelKey(channelKey, function(){
                console.log("Renew channel key successfully");
            }, function(err){
                console.log("Renew channel key failed: ", err);
            });
            }
        });


        client.on('stream-added', function (evt) {
            var stream = evt.stream;
            console.log("New stream added: " + stream.getId());
            console.log("Subscribe ", stream);
            client.subscribe(stream, function (err) {
            console.log("Subscribe stream failed", err);
            });
        });

        client.on('stream-subscribed', function (evt) {
            var stream = evt.stream;
            console.log("Subscribe remote stream successfully: " + stream.getId());
            if (true) {
            $('div#video').append('<div id="agora_remote'+stream.getId()+'" style="width:300px;height:200px;margin-top:-240px;margin-left:-21px;"></div>');
            }
            stream.play('agora_remote' + stream.getId());
        });

        client.on('stream-removed', function (evt) {
            var stream = evt.stream;
            stream.stop();
            $('#agora_remote' + stream.getId()).remove();
            console.log("Remote stream is removed " + stream.getId());
        });

        client.on('peer-leave', function (evt) {
            var stream = evt.stream;
            if (stream) {
            stream.stop();
            $('#agora_remote' + stream.getId()).remove();
            console.log(evt.uid + " leaved from this channel");
            }
        });
        
        }
 },
 
}
</script>
<style>

.camera-btn {
    z-index:10;
    width: 100px;
    height: 50px;
    font-size: 15px;
    background: rgb(8, 191, 145);
    border: 0px;
    position:absolute;   
    margin-left: -50px;
    margin-top: 40px;
    color: white;
}


</style>