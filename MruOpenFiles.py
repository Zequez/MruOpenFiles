import sublime, sublime_plugin
import time, functools

# Gonna do something with AutoHotkey and this
# class MruStopListeningCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#     print("Not listening lalala", time.time())
#     sublime.Settings.set('mru_open_files', 'listening_to_ctrl_tab', False)
 
# class MruStartListeningCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#     print("Listening again", time.time())
#     #sublime.Settings.set('mru_open_files', 'listening_to_ctrl_tab', True)

class MruOpenFilesListener(sublime_plugin.EventListener):
  pending = 0 

  def on_activated(self, view):
    self.pending = self.pending + 1

    move_to_top_timeout = settings.get('move_to_top_timeout')
    # Ask for handleTimeout to be called in 5000ms  
    sublime.set_timeout(functools.partial(self.handle_timeout, view), move_to_top_timeout)
      
  # def on_new(self, view):
  #   self.set_view_as_first(view)

  # def on_load(self, view):
  #   limit_tabs    = settings.get('move_to_top_timeout')
  #   max_open_tabs = settings.get('max_open_tabs')

  #   if limit_tabs and len(sublime.active_window().views()) >= max_open_tabs:
  #     for window_view in sublime.active_window().views()[max_open_tabs:]:
  #       self.close_file(window_view)

  def handle_timeout(self, view):  
    self.pending = self.pending - 1  
    if self.pending == 0:  
      # There are no more queued up calls to handle_timeout, so it must  
      # be the last activated tab
      self.set_view_as_first(view)  
  
  def set_view_as_first(self, view):
    window = sublime.active_window()
    window.set_view_index(view, window.active_group(), 0)

  def close_file(self, view):
    window        = sublime.active_window()
    previous_view = window.active_view()

    window.focus_view(view)
    window.run_command('close_file')
    window.focus_view(view)

def plugin_loaded():
  global settings
  settings = sublime.load_settings('MruOpenFiles.sublime-settings')