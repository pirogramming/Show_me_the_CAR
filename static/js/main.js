const clickLike = (pk, url, csrf_token) => {
  let action = "";
  element = document.getElementById(`like-button${pk}`);
  // element.innerHTML = element.innerHTML == '<i class="fas fa-heart"></i>' ? '<i class="far fa-heart"></i>';
  current_status =
    element.getAttribute("value") == ""
      ? "not_liked"
      : element.getAttribute("value");
  if (current_status == "not_liked") {
    element.setAttribute("value", "liked");
    element.innerHTML = '<i class="fas fa-heart"></i>';
    action = "add_like";
    console.log("liked");
  } else if (current_status == "liked") {
    element.setAttribute("value", "not_liked");
    element.innerHTML = '<i class="far fa-heart"></i>';
    action = "remove_like";
    console.log("disliked");
  }
  $.ajax({
    type: "post",
    url: url,
    data: { pk: pk, action: action, csrfmiddlewaretoken: csrf_token },
    success: () => {
      console.log("success");
    },
    function(request, status, error) {
      // 통신 실패
      alert("fail");
    },
  });
};

const clickEditRating = () => {
  // rateit = document.querySelector(".rateit.rateit-bg");
  // rateBtn = document.querySelector(".jsRateBtn");
  // rateBtn.setAttribute("style", "display: inline-block;");
  // rateit.setAttribute("style", "display: inline-block;");
  // $.ajax({
  //   type: "post",
  //   url: url,
  //   data: {
  //     csrfmiddlewaretoken: csrf_token,
  //   },
  //   success: () => {
  //     console.log("success");
  //   },
  //   function(request, status, error) {
  //     alert("fail");
  //   },
  // });
};

const clickRate = () => {
  // rateit = document.querySelector(".rateit.rateit-bg");
  // rateBtn = document.querySelector(".jsEditRating");
  // rateBtn.setAttribute("style", "display: none;");
  // rateit.setAttribute("style", "display: none;");
};
