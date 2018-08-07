<html>
<head>
<meta charset="utf-8">
  <title>
    시드 X KAU
  </title>
</style>
</head>
<body>
  <div style="text-align:center">
  <font size=20>
  <?php
    echo "<br />\n";
    echo "<br />\n";
    echo "<br />\n";
    echo "<br />\n";
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
    echo "<img src =$var width='900' height='766'/>";
  ?>
</body>
</html>
