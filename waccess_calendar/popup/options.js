$(function() {
	console.log("OPTION");
	$("#semester").change(function () {
		var selected_semester = $(this).val();
		console.log(selected_semester);
	});

	// // selected option persists

	// browser.runtime.sendMessage({type: "check_popup"}, function(response) {
	// 	console.log(response);
	// 	$("#semester option").each(function() {
	// 	  if($(this).text() == response) {
	// 	    $(this).attr('selected', 'selected');
	// 	  }
	// 	})
	// });
});
