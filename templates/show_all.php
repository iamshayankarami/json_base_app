<html>
    <body>
		<?php
		$all_times = {{% times %}}
		for ($i=0; $i<=sizeof($all_times); $i++) {
			echo "<a href=''> $all_times[$i]</a> <br>"
		}
		?>
    </body>
</html>
