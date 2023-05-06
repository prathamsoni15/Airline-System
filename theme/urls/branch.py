from django.urls import path
from ..views.branch import *
branchURL=[
    path('viewBranch/',viewBranch,name="viewBranch"),
    path('addBranch/',addBranch,name="addBranch"),  
    path('updateBranch/<Branch_code>',updateBranch,name="updateBranch"), 
    path('deleteBranch/<Branch_code>',deleteBranch,name="deleteBranch"), 
    path('download_branchcsv',download_branchcsv,name='download_branchcsv'),
]
