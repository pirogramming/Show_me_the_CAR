const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

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

const clickEditRating = (shop_id, el) => {
  thisBtn = el.target;
  cancelEditRatingBtn = document.getElementById(`jsCancelEditRating${shop_id}`);
  thisBtn.setAttribute("style", "display: none;");
  cancelEditRatingBtn.setAttribute("style", "display: block;");

  form = document.getElementById(`jsForm${shop_id}`);
  form.setAttribute("style", "display: block;");
};

const clickCancelEditRating = (shop_id, el) => {
  thisBtn = el.target;
  editRatingBtn = document.getElementById(`jsEditRating${shop_id}`);
  thisBtn.setAttribute("style", "display: none;");
  editRatingBtn.setAttribute("style", "display: block;");

  form = document.getElementById(`jsForm${shop_id}`);
  form.setAttribute("style", "display: none;");
};

const clickRate = (shop_id, url, current_rating, el) => {
  // Prevent refresh
  el.preventDefault();
  el.target.setAttribute("style", "display: none;");

  // Hide Cancelation btn
  cancelEditRatingBtn = document.getElementById(`jsCancelEditRating${shop_id}`);
  thisBtn.setAttribute("style", "display: none;");
  cancelEditRatingBtn.setAttribute("style", "display: none;");

  // Get csrf token
  const csrftoken = getCookie("csrftoken");

  // Get my rating
  rating_element = el.target.querySelector(".rateit-range");
  my_rating = rating_element.getAttribute("aria-valuenow");
  document.getElementById(`jsMyRating${shop_id}`).innerHTML = my_rating;

  // Ajax
  $.ajax({
    type: "post",
    url: url,
    data: {
      shop_id: shop_id,
      my_rating: my_rating,
      csrfmiddlewaretoken: csrftoken,
    },
    success: () => {
      console.log("success");
    },
    function(request, status, error) {
      // 통신 실패
      alert("fail");
    },
  });
  // rateit = document.querySelector(".rateit.rateit-bg");
  // rateBtn = document.querySelector(".jsEditRating");
  // rateBtn.setAttribute("style", "display: none;");
  // rateit.setAttribute("style", "display: none;");
};
