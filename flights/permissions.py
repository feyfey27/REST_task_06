from datetime import date
from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
	message = "Must be owner or staff member to have access!"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (request.user == obj.user): 
			return True
		return False

class UpcomingBookingsOnly(BasePermission):
	message = "3 days minimum."

	def has_object_permission(self, request, view, obj):
		days_left = (obj.date - date.today()).days
		if days_left > 3:
			return True
		return False