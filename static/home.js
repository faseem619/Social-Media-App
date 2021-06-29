function handleMenu() {
  d = document.getElementById("menu_icon");
  s = document.getElementById("non_menu_icons");
  if (d.getAttribute("clicked") == "true") {
    d.style.transform = "rotate(90deg)";
    s.classList.add("menu_active");
    d.setAttribute("clicked", "false");
  } else {
    d.style.transform = "rotate(0deg)";
    d.setAttribute("clicked", "true");
    s.style.animation = "ani2 1s ease-in-out";
    setTimeout(() => {
      s.classList.remove("menu_active");
    }, 1000);
    setTimeout(() => {
      s.style.removeProperty("animation");
    }, 1000);
  }
}

function handleClick(id) {
  num = document.getElementById(id).innerHTML;
  if (document.getElementById(id).getAttribute("data-clicked") === "true") {
    num++;
    document.getElementById(id).innerHTML = num;
    document.getElementById("likes" + id).classList.add("text_glow");
    document.getElementById(id).setAttribute("data-clicked", "false");
  } else {
    num--;
    document.getElementById("likes" + id).classList.remove("text_glow");
    document.getElementById(id).innerHTML = num;
    document.getElementById(id).setAttribute("data-clicked", "true");
  }
  fetch(`${window.origin}/likes`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      num: num,
      id: id,
    }),
  }).then((resp) => console.log(resp));
}

function profilePage(name) {
  location.href = `${window.origin}/home/profiles/${name}`;
}
function toTop() {
  document.body.scrollTop = document.documentElement.scrollTop = 0;
}
window.addEventListener("scroll", () => {
  button = document.querySelector(".back-to-top");
  if (window.scrollY > 280) {
    button.style.display = "block";
  } else {
    button.style.display = "none";
  }
});

window.onload = () => {
  console.log("test");
  if (document.cookie.length != 0) {
    d = document.getElementById("conditional_icon");
    let user = getCookie("username");
    if (d) {
      d.innerHTML =
        '<a href="/home/profiles/' +
        user +
        '"><span class="material-icons-outlined"> account_circle </span></a>';
    }
  }
  /////////////////////
  const dates = document.querySelectorAll(".date");
  const d1 = new Date();
  const year = d1.getFullYear(),
    month = d1.getMonth() + 1,
    day = d1.getDate(),
    hour = d1.getHours(),
    minute = d1.getMinutes(),
    second = d1.getSeconds();
  dates.forEach((element) => {
    const list1 = element.innerHTML.split("/");
    const [postDate, postMonth, rest] = list1;
    const list2 = rest.split(" ");
    const [postYear, rest2] = list2;
    const list3 = rest2.split(":");
    const [postHour, postMinute, postSecond] = list3;
    if (year != postYear) element.innerHTML = `${year - postYear}years ago`;
    else if (month != postMonth)
      element.innerHTML = `${month - postMonth} month${
        month - postMonth > 1 ? "s" : ""
      } ago`;
    else if (day != postDate)
      element.innerHTML = `${day - postDate} day${
        day - postDate > 1 ? "s" : ""
      } ago`;
    else if (hour != postHour)
      element.innerHTML = `${hour - postHour} hour${
        hour - postHour > 1 ? "s" : ""
      } ago`;
    else if (minute != postMinute)
      element.innerHTML = `${minute - postMinute} min${
        minute - postMinute > 1 ? "s" : ""
      } ago`;
    else if (second != postSecond)
      element.innerHTML = `${second - postSecond}s  ago`;
  });
};

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

///////////////////////////////////

function orderPosts(e) {
  type = e.textContent;
  if (!window.location.href.includes("profile")) {
    location.href = `${window.origin}/home/order?type=${type}`;
    return;
  } else {
    address = window.location.href.split("/order");
    location.href = `${address[0]}/order?type=${type}`;
  }
}

if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}

///
