/**
 * Resta Admin Javascript
 * Enhances the admin interface with interactive restaurant-themed elements
 */

document.addEventListener('DOMContentLoaded', function() {
    // Add animation to the welcome message
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.style.opacity = '0';
        welcomeMessage.style.transform = 'translateY(-20px)';
        welcomeMessage.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        
        setTimeout(function() {
            welcomeMessage.style.opacity = '1';
            welcomeMessage.style.transform = 'translateY(0)';
        }, 300);
    }
    
    // Add hover effect to dashboard modules
    const modules = document.querySelectorAll('.dashboard .module');
    modules.forEach(function(module) {
        module.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        
        module.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.2)';
        });
        
        module.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        });
    });
    
    // Add special styling to food-related models in the dashboard
    const modelLinks = document.querySelectorAll('.model-list a');
    modelLinks.forEach(function(link) {
        const text = link.textContent.toLowerCase();
        
        // Add food icons to relevant models
        if (text.includes('menu') || text.includes('dish') || text.includes('food')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-utensils';
            icon.style.marginRight = '8px';
            link.prepend(icon);
        } else if (text.includes('order') || text.includes('reservation')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-receipt';
            icon.style.marginRight = '8px';
            link.prepend(icon);
        } else if (text.includes('customer') || text.includes('client') || text.includes('user')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-user';
            icon.style.marginRight = '8px';
            link.prepend(icon);
        } else if (text.includes('address') || text.includes('location')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-map-marker-alt';
            icon.style.marginRight = '8px';
            link.prepend(icon);
        } else if (text.includes('text') || text.includes('content')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-file-alt';
            icon.style.marginRight = '8px';
            link.prepend(icon);
        }
    });
    
    // Enhance form submit buttons with animation
    const submitButtons = document.querySelectorAll('.submit-row input');
    submitButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            this.style.transition = 'transform 0.2s ease';
            this.style.transform = 'scale(0.95)';
            
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 200);
        });
    });
    
    // Add a nice toast notification system
    function createToast(message, type = 'info') {
        // Only create if we have a message
        if (!message) return;
        
        // Create toast container if it doesn't exist
        let toastContainer = document.getElementById('toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.id = 'toast-container';
            toastContainer.style.position = 'fixed';
            toastContainer.style.bottom = '20px';
            toastContainer.style.right = '20px';
            toastContainer.style.zIndex = '10000';
            document.body.appendChild(toastContainer);
        }
        
        // Create the toast element
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.style.backgroundColor = type === 'success' ? '#556B2F' : 
                                      type === 'error' ? '#CD5C5C' : 
                                      type === 'warning' ? '#DEB887' : '#8B4513';
        toast.style.color = 'white';
        toast.style.padding = '10px 15px';
        toast.style.marginBottom = '10px';
        toast.style.borderRadius = '4px';
        toast.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.2)';
        toast.style.display = 'flex';
        toast.style.alignItems = 'center';
        toast.style.justifyContent = 'space-between';
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(20px)';
        toast.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        
        // Add appropriate icon
        const icon = document.createElement('i');
        icon.className = type === 'success' ? 'fas fa-check-circle' : 
                         type === 'error' ? 'fas fa-times-circle' : 
                         type === 'warning' ? 'fas fa-exclamation-triangle' : 'fas fa-info-circle';
        icon.style.marginRight = '10px';
        
        // Add message
        const messageSpan = document.createElement('span');
        messageSpan.textContent = message;
        
        // Add close button
        const closeBtn = document.createElement('button');
        closeBtn.style.background = 'none';
        closeBtn.style.border = 'none';
        closeBtn.style.color = 'white';
        closeBtn.style.marginLeft = '10px';
        closeBtn.style.cursor = 'pointer';
        closeBtn.innerHTML = '&times;';
        closeBtn.onclick = function() {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(20px)';
            setTimeout(() => {
                toast.remove();
            }, 300);
        };
        
        // Assemble toast
        toast.appendChild(icon);
        toast.appendChild(messageSpan);
        toast.appendChild(closeBtn);
        
        // Add to container
        toastContainer.appendChild(toast);
        
        // Show with animation
        setTimeout(() => {
            toast.style.opacity = '1';
            toast.style.transform = 'translateY(0)';
        }, 10);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (toast && toast.parentNode) {
                toast.style.opacity = '0';
                toast.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    if (toast && toast.parentNode) {
                        toast.remove();
                    }
                }, 300);
            }
        }, 5000);
    }
    
    // Display any Django messages as toasts
    const djangoMessages = document.querySelectorAll('.messagelist li');
    if (djangoMessages.length > 0) {
        djangoMessages.forEach(message => {
            let type = 'info';
            if (message.classList.contains('success')) {
                type = 'success';
            } else if (message.classList.contains('error')) {
                type = 'error';
            } else if (message.classList.contains('warning')) {
                type = 'warning';
            }
            
            createToast(message.textContent, type);
        });
        
        // Optionally hide the original messages
        const messageList = document.querySelector('.messagelist');
        if (messageList) {
            messageList.style.display = 'none';
        }
    }
    
    // Welcome toast on admin index page
    const isIndexPage = document.querySelector('.dashboard');
    if (isIndexPage) {
        createToast('Welcome to Resta Administration', 'success');
    }
    
    // Add a "Today's Special" indicator to the latest added menu item (if applicable)
    const isMenuItemPage = window.location.href.indexOf('menuitem') > -1;
    if (isMenuItemPage && document.querySelector('table')) {
        const firstRow = document.querySelector('tbody tr:first-child');
        if (firstRow) {
            const specialBadge = document.createElement('span');
            specialBadge.textContent = "Today's Special";
            specialBadge.style.backgroundColor = '#CD5C5C';
            specialBadge.style.color = 'white';
            specialBadge.style.padding = '3px 8px';
            specialBadge.style.borderRadius = '12px';
            specialBadge.style.fontSize = '10px';
            specialBadge.style.fontWeight = 'bold';
            specialBadge.style.marginLeft = '10px';
            
            const firstCell = firstRow.querySelector('th') || firstRow.querySelector('td');
            if (firstCell) {
                firstCell.appendChild(specialBadge);
            }
        }
    }
}); 