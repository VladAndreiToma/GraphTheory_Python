'''
def Count_Isolated_Islands( image ):
    # giving an array of pixels 1 and 0 count as many isolated islands as possible
    # an island is represented by a 1 pixel that has 0 as neighbours top bottom left and right
    # the case of a single element
    if len( image ) == 1:
        if image[0][0] == 0:
            return 0
        elif image[0][0] == 1:
            return 1
        else:
            pass
    IsoIslNo = 0
    # the case of 2/2 matrix:
    # checking the corners
    if len( image ) == 2:   # i forgot to mention that the matrix is square each time
        if image[0][0] == 1 and image[0][1] == 0 and image[1][0] == 0:
            IsoIslNo += 1
        if image[0][1] == 1 and image[0][0] == 0 and image[1][1] == 0:
            IsoIslNo += 1
        if image[1][0] == 1 and image[0][0] == 0 and image[1][1] == 0:
            IsoIslNo += 1
        if image[1][1] == 1 and image[1][0] == 0 and image[0][1] == 0:
            IsoIslNo += 1
    if len( image ) > 2:
        # then the image matrix is bigger than 2/2 so border has to analyzed
        # also the interiors
        # use a counter to count for linkings inside the border
        # if it is bigger than 2 then NOT increase the value of IsoIslNo
        for i in range( 1 , len(image)-1 ):
            for j in range( 1 , len(image)-1 ):
                counter = 0
                if image[i][j] == 1:
                    # count for linkings wiht other image cells
                    if image[i-1][j] == 1:
                        counter += 1 # up condition
                    if image[i+1][j] == 1:
                        counter += 1 # down condition
                    if image[i][j-1] == 1:
                        counter += 1 # left condition
                    if image[i][j+1] == 1:
                        counter += 1 # right condition
                    if counter < 2:
                        IsoIslNo += 1
        # now inspect the first line without corners
        i = 0
        for j in range( 1 , len(image)-1 ):
            counter = 0
            if image[i][j] == 1:
                # left right underneath
                if image[i+1][j] == 1:
                    counter += 1
                if image[i][j-1] == 1:
                    counter += 1
                if image[i][j+1] == 1:
                    counter += 1
                if counter < 2:
                    IsoIslNo += 1
        # now inspect the last line don t account for corners
        i = len(image)-1
        for j in range( 1 , len(image)-1 ):
            counter = 0 # for each element
            if image[i][j] == 1:
                # look up left and right
                if image[i-1][j] == 1:
                    counter += 1
                if image[i][j-1] == 1:
                    counter += 1
                if image[i][j+1] == 1:
                    counter += 1
                if counter < 2:
                    IsoIslNo += 1
        # now inspect first column dont account for corners
        j = 0
        for i in range( 1 , len(image) - 1):
            counter = 0 # for each element
            if image[i][j] == 1:
                # look up down and right
                if image[i][j+1] == 1:
                    counter += 1
                if image[i-1][j] == 1:
                    counter += 1
                if image[i+1][j] == 1:
                    counter += 1
                if counter < 2:
                    IsoIslNo += 1
        # now inspect the last column dont account for corners
        j = len(image)-1
        for i in range( len(image) - 1):
            counter = 0 # for each element
            if image[i][j] == 1:
                # look up down and left
                if image[i][j-1] == 1:
                    counter += 1
                if image[i-1][j] == 1:
                    counter += 1
                if image[i+1][j] == 1:
                    counter += 1
                if counter < 2:
                    IsoIslNo += 1
        # now account for corners:   0 , 0     0 , len-1      len-1 , 0    len-1 , len-1
        if image[0][0] == 1:
            if image[1][0] == 0 and image[0][1] == 0:
                IsoIslNo += 1
        if image[0][len(image)-1] == 1:
            if image[1][len(image)-1] == 0 and image[0][len(image)-2] == 0:
                IsoIslNo += 1
        if image[len(image)-1][0] == 1:
            if image[len(image)-2][0] == 0 and image[len(image)-1][1] == 0:
                IsoIslNo += 1
        if image[len(image)-1][len(image)-1] == 1:
            if image[len(image)-2][len(image)-1] == 0 and image[len(image)-1][len(image)-2] == 0:
                IsoIslNo += 1

    return IsoIslNo
'''

'''
def Count_Isolated_Islands( image ):
    if not image or not image[0]:
        return 0
    rows, cols = len(image), len(image[0])
    visited = [[False] * cols for _ in range(rows)]
    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols
    def dfs(i, j):
        if not is_valid(i, j) or visited[i][j] or image[i][j] == 0:
            return
        visited[i][j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir_i, dir_j in directions:
            new_i, new_j = i + dir_i, j + dir_j
            dfs(new_i, new_j)
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == 1 and not visited[i][j]:
                island_count += 1
                dfs(i, j)

    return island_count

print( Count_Isolated_Islands( [[1 , 1 , 0 , 0, 0], [1, 1, 0 , 0 , 0], [1,1,0, 0, 0] , [0,0,1,1,1] , [ 0 , 0 , 1 , 1 , 1]] ))
'''



# 1 . This code returns the longest chain in a unweighted graph: ====================================================================================================================
def Connected_Components( myGraph ):
    # undirected graph ----> adjacent matrix symmetric with respect to both diagonals
    # find the chain/s of connected elements
    if not myGraph or not myGraph[0]:
        return "No components"
    rows , cols = len(myGraph) , len( myGraph[0] )
    # make a visitation array to avoid infinite loops ---> initialize it as False
    visited = [ [False] * cols for _ in range( rows ) ]
    def position_is_valid( i , j ):
        # check if the current position in nout out of bounds
        return 0 <= i < rows and 0 <= j < cols
        # true if not out of bonds , false otherwise
    def DFS( i , j ):
        # the depth first search function will start from a node i , j
        # should be valid if not out of bonds and not visited and not 0   .. 0 represents no connection 1 represents connection in adjacent matrices
        if not position_is_valid( i , j ) or visited[i][j] or myGraph[i][j] == 0:
            return 0 # go back one step on the stack
        visited[i][j] = True  # i am in the current node
        current_chain = 1
        WhereTo = [ (0, 1) , (0, -1) , (1, 0) , (-1, 0)]
        for dirI, dirJ in WhereTo: #couples to form up down left right
            newI , newJ = i + dirI , j + dirJ
            current_chain += DFS( newI , newJ )
        return current_chain
    max_chain = 0
    for i in range( rows ):
        for j in range( cols ):
            # if i have a starting point of 1
            if myGraph[i][j] == 1 and not visited[i][j]: # never started here
                current_chain = DFS( i,j )
                max_chain = max( max_chain , current_chain )

    return max_chain

print( Connected_Components( [ [1, 0, 1, 0],[1, 1, 0, 0],[0, 0, 1, 1], [0, 1, 0, 0] ] ))
# this code provides a little bit of DFS usage
# using Depth First Search one can easily get the adjacent neighbours of one node that
# starts with one to account for all connected pieces of land to make a cluster of islands
# a cluster can make an individual island if separated from the others with the condition that
# top right left and bottom imply no passage between islands
# ===================================================================================================================================================================================================


# ===================================================================================================================================================================================================
# 2. This code solves the existence of a cycle in an unw graph that is oriented
def Check_For_Cycle( myGraph ):
    if not myGraph or not myGraph[0]:
        return "No components"

    rows, cols = len(myGraph), len(myGraph[0])
    visited = [[False] * cols for _ in range(rows)]

    def position_is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def DFS(i, j):
        if not position_is_valid(i, j) or visited[i][j] or myGraph[i][j] == 0:
            return None  # return None if the current position is invalid or already visited or contains 0
        visited[i][j] = True
        WhereTo = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = None
        for dirI, dirJ in WhereTo:
            newI, newJ = i + dirI, j + dirJ
            result = DFS(newI, newJ)
            if result is not None:
                break  # Found a final node, exit the loop
        return result if result is not None else (i, j)

    final_node = None
    for i in range(rows):
        for j in range(cols):
            if myGraph[i][j] == 1 and not visited[i][j]:
                final_node = DFS(i, j)
                if final_node is not None:
                    break  # Found a final node, exit the loop
        if final_node is not None:
            break  # Found a final node, exit the outer loop

    return f"Final (i,j) is: {final_node}"

print( Check_For_Cycle( [[1,1,1] , [0,0,1] , [0,1,1]] ))
