import json
import sys



def main():
    data = {"data":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquet lorem id arcu facilisis euismod. Duis congue lectus eget urna gravida pellentesque. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum condimentum dapibus ex, ut fermentum tellus convallis vel. Suspendisse tincidunt mauris a ex consectetur ultricies. Suspendisse potenti. Morbi semper nulla non lectus lacinia, eget sagittis mauris fermentum. Aliquam maximus vel magna id sodales. Fusce vitae euismod libero, ut feugiat orci. Sed ullamcorper purus orci, vitae faucibus magna volutpat sit amet. Phasellus dapibus scelerisque posuere. Aenean nec condimentum ligula. Pellentesque hendrerit, ipsum ut finibus commodo, ipsum lorem mattis dolor, nec rutrum sem velit sit amet arcu.\n Aliquam varius mauris non suscipit consectetur. Proin vehicula orci id lobortis convallis. Aenean facilisis, quam vitae eleifend mollis, erat nisl accumsan turpis, eu tempor sapien orci quis neque. Nam sed congue sem, eu commodo tortor. Morbi ornare dolor ut lectus posuere, elementum vestibulum nisl luctus. Nam tincidunt, purus id feugiat porta, magna nibh pretium dolor, eu tristique erat erat eu dolor. Quisque urna metus, gravida vel semper nec, fermentum sed justo. Suspendisse ex quam, convallis vel felis quis, dictum lacinia augue. Suspendisse quis mollis turpis. Quisque lobortis, nisi sed pharetra lacinia, urna dolor sodales est, in molestie sapien ex a magna. Nullam sit amet enim sapien. Fusce fringilla, orci eu porttitor elementum, magna orci auctor libero, ut consequat leo felis id sem. Nam ut lacus vel ligula feugiat placerat et at est.\n Pellentesque auctor bibendum arcu non mollis. Sed at ante maximus, laoreet tortor ac, sollicitudin ipsum. Proin lorem elit, commodo sed turpis a, dignissim euismod enim. Morbi eu leo eget lectus varius auctor volutpat non ante. Nam euismod, leo sed accumsan pharetra, dui neque auctor magna, a elementum magna sapien maximus felis. Phasellus vel lacus ullamcorper, faucibus tellus eget, pharetra turpis. Ut ut imperdiet risus. Quisque congue odio ac odio fermentum congue.\n Sed non urna ornare, tempor elit id, lacinia felis. Maecenas pharetra leo sit amet gravida tincidunt. Maecenas mollis mauris id maximus porttitor. Suspendisse dui libero, eleifend quis condimentum non, consequat vel felis. Phasellus facilisis eu lacus vel tristique. Donec eleifend mauris quis ante semper feugiat. Nam congue tempor augue eu mattis. Donec tristique posuere metus. Etiam scelerisque dolor finibus dui scelerisque, nec imperdiet tellus condimentum. Maecenas erat libero, finibus ut eleifend nec, imperdiet id ligula. Sed ac aliquam enim, eu sollicitudin turpis. Vestibulum id dui vitae nulla malesuada volutpat. Quisque semper nisl vitae nunc pellentesque auctor.\n Nunc ut tempus ante. Maecenas at quam in massa faucibus laoreet id sit amet turpis. Nullam semper lorem ut mi venenatis, non interdum velit tempor. Morbi maximus enim eget nunc condimentum dictum. Nulla facilisis sem nisl, tincidunt sagittis orci maximus in. Donec iaculis, risus sed scelerisque placerat, diam risus fringilla risus, laoreet interdum quam lorem nec eros. Ut imperdiet dignissim neque in bibendum. Nunc molestie gravida est. Vestibulum et elit quis diam fringilla commodo non id dolor. Aenean rhoncus mauris eu gravida mollis."}
    
    while True:
        json.dump(data, sys.stdout, indent=4)



if __name__ == '__main__':
    main()
