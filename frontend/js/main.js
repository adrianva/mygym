var CONFIG = (function() {
     var IP = 'http://127.0.0.1:8000';
     var private = {
         'IP': 'http://127.0.0.1:8000',
         'API_PLANS': IP + '/api/plans/',
         'API_EXERCISES': IP + '/api/exercises/'
     };

     return {
        get: function(name) { return private[name]; }
    };
})();


function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function addExercise(elementID) {
    console.log(elementID);
    //$('#list-plans').html("<a class='list-group-item' href='#'>data[index].plan_name</a>");
    $(elementID).html(
        '<div class="form-group">' +
        '<label class="col-md-4 control-label" for="select-exercise">Exercise</label>' +
        '<div class="col-md-4"> <select id="select-exercise" name="select-exercise" class="form-control">' +
        '</select></div></div>' +
        '<div class="form-group">' +
        '<label class="col-md-4 control-label" for="exercise-duration">Duration</label>' +
        '<div class="col-md-4">' +
        '<input id="exercise-duration" name="exercise-duration" type="text" placeholder="Duration of the Exercise (seconds)" class="form-control input-md" required="">' +
        '</div></div>'
    );
}


// Submit csv on submit
$('#form-plan').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    createPlan();
});


// AJAX for post a plan
function createPlan() {
    console.log("create_plan is working!"); // sanity check
    var data = $('#form-plan').serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});
    console.log(data);
    $.ajax({
        url: CONFIG.get('API_PLANS'), // the endpoint
        type: "POST", // http method
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({
            plan_name: data["plan-name"],
            plan_description: data["plan-description"],
            plan_difficulty: data["plan-difficulty"],
            days: [{
                day_name: data["day-name"],
                order: 1,
                exercises: [{
                    day: {},
                    exercise: data["select-exercise"],
                    exercise_duration: data["exercise-duration"],
                    order: 1
                }],
                plan: {}
            }]
        }),

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            $('#feedback').html("<div class='alert alert-success'>Plan successfully created!"); // add the success msg to the dom
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr) {
            $('#feedback').html("<div class='alert alert-danger'>Oops! We have encountered an error."); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}