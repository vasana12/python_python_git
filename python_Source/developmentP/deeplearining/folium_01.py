import folium

# 서울 시청을 중심으로 하는 지도 생성
map_osm = folium.Map(location=[37.566345, 126.977893])
map_osm.save('map1.html') # 지도 저장

# zoom_start : 지도 크기 설정
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start= 17)
map_osm.save('map2.html')

# 포리움은 기본적으로 'Open Street Map' 을 기반으로 동작하지만 내부적으로는 'Stamen Terrain',
# 'Stamen Toner' , 'Mapbox Bright' , 와 'Mapbox Control room tiles' 형식을 내장하고 있다.
map_osm = folium.Map(location=[36.566345, 126.977893], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('map3.html')

map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17, tiles='Stamen Toner')
map_osm.save('map4.html')

#지도 마커 설정
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='서울특별시청').add_to(map_osm)
folium.Marker([37.5658879, 126.9754788], popup='덕수궁').add_to(map_osm)

map_osm.save('map5.html')
map_som = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='서울특별시청',
              icon = folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859, 126.9754788], radius=100, color='#3186cc',
                    fill_color='#3186cc', popup='덕수궁').add_to(map_osm)
map_osm.save('map6.html')