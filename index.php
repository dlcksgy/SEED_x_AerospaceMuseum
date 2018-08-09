<html>
<head>
<meta charset="utf-8">
<meta name="HandheldFriendly" content="true"/>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
  <title>
    시드 X KAU
  </title>
</style>
</head>
<body>
  <script>
    $(document).on('touchmove', false);
  </script>
  <div style="background-color:gray; width:100%; height:10%; font-size:30px; text-align:center; color:aqua">디자인작업중입니다</div>
  <div style="text-align:center">
  <font size=4>
  <?php
    echo "<br />\n";
//    echo "<br />\n";
//    echo "<br />\n";
//    echo "<br />\n";
  ?>
    아래 바코드를 바코드스캐너에 갖다대세요
  </font>
  </div>
  <?php
    include_once 'lib/image_proc.function.php';
    echo "<br />\n";
    echo "<br />\n";
    echo "<br />\n";
    $var= exec("python barcode.py");
    echo "<img src =$var width='100%' height='20%'/>";
  ?>
</body>
</html>
