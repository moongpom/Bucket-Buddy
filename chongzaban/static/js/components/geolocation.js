var geocoder = new kakao.maps.services.Geocoder();
var displayAddress = document.getElementById('display-address');

function setAddress(city, gu, dong) {
  displayAddress.value = city + ' ' + gu + ' ' + dong;
};

function onGeoSuccess(position) {
  const lat = position.coords.latitude;
  const lng = position.coords.longitude;
  geocoder.coord2Address(lng, lat, function(result, status){
    if (status === kakao.maps.services.Status.OK) {
      setAddress(result[0].address.region_1depth_name, result[0].address.region_2depth_name, result[0].address.region_3depth_name);
    }
  });
};

function onGeoError() {
  alert("위치 정보를 찾을 수 없습니다.");
};

navigator.geolocation.getCurrentPosition(onGeoSuccess, onGeoError);