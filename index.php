<html>
<head>
<meta charset="utf-8">
<meta name="HandheldFriendly" content="true"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
  <title>
    시드 X KAU
  </title>
</style>
</head>
<body style="margin:0px;">
<div style="background-color:black; border:3px solid black; padding:8px">
  <script>
    $(document).on('touchmove', false);
  </script>
  <div style="background-color:black; padding:5px; margin:0px">
    <div style="width:100%; height:10%; font-size:30px; text-align:center; color:white">
       <img src="img_res\seed_logo.png" width="40px" height="40px" /> SEEDx항공우주박물관
    </div>
  </div>
  <div style="text-align:center">
  <div style="font-size:20px; color:white">
  <?php
    echo "<br />\n";
//    echo "<br />\n";
//    echo "<br />\n";
//    echo "<br />\n";
  ?>
    아래 바코드를 바코드스캐너에 갖다대세요
  </div>
  </div>
  <?php
    include_once 'lib/image_proc.function.php';
//    echo "<br />\n";
//    echo "<br />\n";
    echo "<br />\n";
    $var= exec("python barcode.py");
    echo "<img src =$var width='100%' height='20%'/>";
  ?>
  <img src="img_res\Press_Start_Gaming-Blog.gif" width="100%"/>
<!--  <img src="img_res\retro_games.jpg" width="100%"/>-->
</div>
</body>
</html>
